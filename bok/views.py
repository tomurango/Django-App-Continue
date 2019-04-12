from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from bok.models import Player, Job, Task, Skill
from django.contrib.auth.models import User
import uuid

# Create your views here.
@login_required
def home(request):
    if Player.objects.filter(user=request.user).exists():
        try:
            main_job=Job.objects.get(player_num=Player.objects.get(user=request.user), main=1)
            job_data={'job':main_job,'tasks':Task.objects.all()}
            return render(request, 'bok/home.html',job_data)
        except:
            return render(request, 'bok/home.html')
    return render(request, 'bok/home.html')

@login_required
def mybok(request):
    """top"""
    return render(request, 'bok/mybok.html')

@login_required
def private_page(request):
    return render(request, 'bok/private.html', {})

def public_page(request):
    return render(request, 'bok/public.html', {})

@login_required
def sign_up(request):
    if request.method == "POST":
        namer=request.POST['namer']
        #ここで、name がすでにある場合を判定して if 分岐
        if Player.objects.filter(user=request.user).exists():
            Player.objects.filter(user=request.user).update(name=namer)
            job=Job.objects.get(player_num=Player.objects.get(user=request.user), main=1)

        #申請する処理
        #pipelineの実装でいらなくなったかも
        else:
            data=Player(name=namer,user=request.user)
            data.save()
            fjob=Job(name="無職",explain="文字通りの無職",player_num_id=data.id)
            fjob.save()
            return render(request, 'bok/home.html',{'job':fjob,'tasks':Task.objects.all()})
        return render(request, 'bok/home.html',{'job':job,'tasks':Task.objects.all()})
    else:
        #冒険をはじめるめる処理
        return render(request, 'bok/signup.html')

@login_required
def job_des(request):
    if request.method == "POST":
        num=Player.objects.get(user=request.user)
        #すでに、外部キーを持つジョブがある場合 main 変数を変更
        if Job.objects.filter(player_num=num,main=1).exists():
            Job.objects.filter(player_num=num,main=1).update(main=0)
        #Job の登録
        name=request.POST['name']
        expl=request.POST['expl']
        toke=request.POST['submit_token']
        new=Job(name=name,explain=expl,player_num=num,token=toke)
        try:
            new.save()
            main_job=Job.objects.get(player_num=Player.objects.get(user=request.user), main=1)
            job_data={'job':main_job,'tasks':Task.objects.all()}
            return render(request,'bok/home.html',job_data)
        except:
            main_job=Job.objects.get(player_num=Player.objects.get(user=request.user), main=1)
            job_data={'job':main_job,'tasks':Task.objects.all()}
            return render(request,'bok/home.html',job_data)
    
    main_job=Job.objects.get(player_num=Player.objects.get(user=request.user), main=1)
    submit_token=uuid.uuid4()
    job_data={'job':main_job,'submit_token':submit_token,'tasks':Task.objects.all()}
    return render(request, 'bok/job.html',job_data)

@login_required
def task(request):
    #POST メソッドの処理
    if request.method == "POST":
        player=Player.objects.get(user=request.user)
        job=Job.objects.get(player_num=player, main=1)

        #form の値を取得する
        name=request.POST['what']
        time=request.POST['time']
        toke=request.POST['submit_token']
        #クラスを作成
        new_task=Task(what=name,time=time,player_num=player,Job_num=job,token=toke)
        #データベースに保存
        #ユニークエラーが出なかったら
        try:
            new_task.save()
            #job のレベル上げ
            #expに経験値を代入して扱う
            exp=job.xp
            #timeの値を上乗せする
            exp += int(time)
            #n に100引いた回数を計算してもらう
            n=0
            while exp >= 100:
                exp -= 100
                n+=1
            #jobのレベル取得
            lv=job.level
            lv+=n
            #xpとjobのアップデート
            Job.objects.filter(player_num=player, main=1).update(level=lv,xp=exp)
            
            #nが1より大きい場合スキルを付与する
            if n >= 1:
                skill=job.skillpoint
                #スキルポイントは1レベル当たり1ポイントに設定されています
                skill+=n
                #skillpointのアップデート
                Job.objects.filter(player_num=player, main=1).update(skillpoint=skill)
        #エラー出たら(tokenのuniqueエラーだと思う)
        except:
            #特に保存しない
            a=1
        return render(request,'bok/home.html',{'job':Job.objects.get(player_num=player, main=1),'tasks':Task.objects.all()})
    submit_token=uuid.uuid4()
    return render(request,'bok/task.html',{'submit_token':submit_token})

@login_required
def job_name(request):
    if request.method =="POST":
        #playerの情報を取得する
        player=Player.objects.get(user=request.user)
        #form の値を取得する
        name=request.POST['newname']
        expl=request.POST['newexpl']
        #job の名前と説明をアップデート
        Job.objects.filter(player_num=player, main=1).update(name=name,explain=expl)
        #jobのデータをhomeにわたす
        main_job=Job.objects.get(player_num=Player.objects.get(user=request.user), main=1)
        job_data={'job':main_job,'tasks':Task.objects.all()}
        return render(request,'bok/home.html',job_data)
    return render(request,'bok/jobname.html')

@login_required
def job_change(request):
    #playerの情報を取得
    player=Player.objects.get(user=request.user)
    #jobの情報取得
    main_job=Job.objects.get(player_num=player,main=1)
    if request.method == "POST":
        #mainjobのmainを0にして、取得したjobのmainを1にする
        Job.objects.filter(player_num=player,main=1).update(main=0)
        #homeに新しいmainjobの情報を流す
        Job.objects.filter(player_num=player,id=int(request.POST['newjob'])).update(main=1)
        return render(request,'bok/home.html',{'job':Job.objects.get(player_num=player,main=1),'tasks':Task.objects.all()})
    your_jobs=Job.objects.filter(player_num=player,main=0)
    job_dict={
        'main':main_job,
        'sub':your_jobs
    }
    return render(request,'bok/jobchange.html',job_dict)

@login_required
def skill(request):
    #playerの取得
    player=Player.objects.get(user=request.user)
    #jobの取得
    main_job=Job.objects.get(player_num=player, main=1)
    #Skill Pointが0の時、お断りの処理
    if main_job.skillpoint == 0:
        return render(request,'bok/home.html',{'job':main_job,'tasks':Task.objects.all()})
    #POSTの時
    if request.method == "POST":
        #jobのアップデート
        n=main_job.skillpoint
        n-=1
        Job.objects.filter(player_num=player, main=1).update(skillpoint=n)
        #Skillの作成
        name=request.POST['name']
        expl=request.POST['expl']
        toke=request.POST['submit_token']
        new_skill=Skill(name=name,explain=expl,Job_num=main_job,token=toke)
        try:
            new_skill.save()
        except:
            a=1
        return render(request,'bok/home.html',{'job':Job.objects.get(player_num=player, main=1),'tasks':Task.objects.all()})
    submit_token=uuid.uuid4()
    return render(request,'bok/skill.html',{'job':main_job,'tasks':Task.objects.all(),'submit_token':submit_token})