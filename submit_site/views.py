
from django.contrib.auth.models import User
from django.conf import settings
from django.shortcuts import redirect
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from . import test_site as ts
#from . import post_obj_ops as po
from .models import Properties
from .forms  import PicForm


def assemble_post_views(prop_obj):
    p = prop_obj

    frame = """
    <br/><div style = "height: auto; width: 60%; border: 1px black solid; border-rotation: 5px; box-shadow: 3px grey;">
    <img src = "{image}" style = ></img>
    property_name: {prop_name}<br/>
    posted_by {broker} on {postdate}<br/>
    description: {description}<br/>
    contact: {phone_num}
    last modified on {last_mod}
    <ul style = "list-style-type: none"> 
    <li><a href = "/submit/edit?del=1&ed=0&ord={pk}"> delete </a></li>  <!-- Needs a Conf Dialogue -->
    <li><a href = "/submit/edit?del=2&ed=1&ord={pk}"> edit </a></li>
    </ul>
    <!--
    <a href = ""> view translation </a> --><!-- This is going to go to a js script-->
    </div><br/>>
    """.encode('utf-8')

    return unicode(frame).format(image ='/media/' + str(p.pics),
                        prop_name = p.property_name,
                        broker = p.broker_name,
                        postdate = p.post_date,
                        description = p.description,
                        phone_num = p.phone_number,
                        last_mod = p.last_edit,
                        pk = str(p.pk)
                        )



def submit(request):

    print request.user.is_authenticated()
    if not request.user.is_authenticated():
        return redirect(settings.LOGIN_URL, request.path)

    commands = request.GET

    status = ""
    # This takes care of the account verification
    account_hash = request.user.username
    print dir(account_hash) 

    #AUTH shit goes here
   

    #Handles Post Bullshit
 
    
    
    pic_form = PicForm(request.POST, request.FILES)    
    
    print pic_form.is_valid()

    if request.method == 'POST' and pic_form.is_valid():
        db_fetch = Properties()
        prop_info = request.POST         
        
        if pic_form.is_valid():
            db_fetch.pics = request.FILES['picform']     
        print request.FILES
   
        db_fetch.account_ref = account_hash
        db_fetch.broker_name = prop_info["broker_name"]
        db_fetch.property_name = prop_info["prop_name"]
        db_fetch.description = prop_info["description"]
        db_fetch.phone_number = prop_info["phone_number"]        
        db_fetch.save() 
        status = "Post Submitted" 

    else:
        status = "Enter Info to add to Korestate DB"
    
    
    test_site = ts.test_site()
    post_list = Properties.objects.order_by('post_date')
    post_list = ''.join([assemble_post_views(post) for post in post_list if post.account_ref == account_hash])
    template = "index.html" 

    
    context = {"submit_form" : test_site,
                "post_list" : post_list,   
                "status" : status,
                "image_form" : PicForm(request.POST, request.FILES)  
              } 
   
    return render(request,template,context)



def edit_manager(request):  #No status return yet
    commands = request.GET
    try:
        command_list = tuple(commands[key] for key in commands)
        print ":::///Taking from Get:", command_list
        if len(command_list) < 2:
            return HttpResponseRedirect('/submit')
        
        #Delete Mode
        print 'COMMANDS',commands 
        if commands[u'del'] == u'1':
            try:
                Properties.objects.all().filter(pk = int(commands['ord'])).delete()
                return HttpResponseRedirect('/submit')
 
            except:
                return HttpResponseRedirect('/submit')

        #Edit Mode
        if commands[u'ed'] == u'1':
            print "EDIT RECEIVED"
            #Properties.objects.all().filter(pk = int(commands['ord']))
            
            redirect_string = '/submit/edit/page?ed=1&ky={key}'.format(key = int(commands['ord']))
            return HttpResponseRedirect(redirect_string)
            
    except:
        print "ERROR in edit_manager"
        return HttpResponseRedirect('/submit')
       


def edit_mode(request):
    print "EDIT MODE"
    print "NEW REQ,", request.GET
    status = "Please Type Changes and click submit."
    try:
        if request.GET['revisions'] == 't':
            update_req = request.POST
            print "REQ INFO", update_req
            to_update = Properties.objects.all().filter(pk = update_req[u'pk'])[0]
            print "UPDATING...", to_update
            to_update.broker_name = update_req[u'broker_name'] 
            to_update.property_name = update_req[u'property_name']
            to_update.description = update_req[u'description']
            to_update.radio_array = update_req[u'radio_array']
            to_update.save()
            status = "Changes Successfully Made  <a href = '/submit'> go back</a> "

    except:
        status = "Update error"
    
    try:
        edit_conf = request.GET['ed']
        edit_key = request.GET['ky']
               

    except:
        return HttpResponseRedirect('/accounts/fail?err=Database Error 404::Bad Navigation')
    

    db_fetch = Properties.objects.all().filter(pk=edit_key)[0]
    template = "edit_site.html"
    prop_sheet = {
        "pk" : db_fetch.pk,
        "pics" : db_fetch.pics,     
        "broker_name" : db_fetch.broker_name,
        "property_name" : db_fetch.property_name,
        "description" :  db_fetch.description,
        "phone_number" :  db_fetch.phone_number,
        "radio_array" :   db_fetch.radio_array,      
        "status" : status
    }

    return render(request, template, prop_sheet)
