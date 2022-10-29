from django.shortcuts import render
import pusher

pusher_client = pusher.Pusher(
  app_id='1497231',
  key='82433bfd69df6eaab70a',
  secret='13ef0c84e012f7c2123f',
  cluster='ap2'
)
def index(request):
    pushed_text = request.POST.get('text')
    my_dict = {'message': pushed_text}
    pusher_client.trigger('my-channel', 'my-event', my_dict)
    return render(request, 'app/main.html')