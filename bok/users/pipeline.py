from bok.models import Player, Job
import uuid

def get_avatar(backend, strategy, details, response,
        user=None, *args, **kwargs):
    url = None
    if backend.name == 'facebook':
        url = "http://graph.facebook.com/%s/picture?type=large"%response['id']
    if backend.name == 'twitter':
        url = response.get('profile_image_url', '').replace('_normal','')
    if backend.name == 'google-oauth2':
        url = response['picture']
        name = response['name']
    if url:
        data=Player(name=name,user=user,avatar=url)
        try:
            data.save()
            token = uuid.uuid4()
            fjob=Job(name="無職",explain="文字通りの無職",player_num_id=data.id,token=token)
            fjob.save()
            #playerのログイン時のUnique error対策
            #いつかの挙動不審の原因の可能性あり
        except:
            a=1