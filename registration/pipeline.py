def get_profile_picture(backend, user, response, details, is_new=False, *args, **kwargs):
    img_url = None
    if backend.name == 'facebook':
        img_url = 'http://graph.facebook.com/%s/picture?type=large' \
            % response['id']
    # elif backend.name == 'linkedin-oauth2':
    #     img_url = response.get('profile_image_url', '').replace('_normal', '')
    user.image = img_url
    user.save()
