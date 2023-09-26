from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages as msg
from django.core.mail import send_mail


# Create your views here.
def home(request):
    return render(request, "index.html", {"user_logged": request.session.has_key('user_logged')})


def contactUs(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        tel = request.POST['tel']
        add = request.POST['address']
        grade = request.POST['class']
        fee = request.POST['fee']
        msg = request.POST['message']

        cs = ContactUS
        obj = cs(name=name, grade=grade, email=email, phone=tel, add=add, fee=fee, add_n=msg)
        obj.status = 0
        obj.tuID = "# IGH-0" + str(len(cs.objects.all()))
        obj.save()

        mesg = f"Name: {name} \nPhone: {tel} \nEmail: {email} \nAddress: {add} \nGrade {grade} \nFees {fee} \nAdditional Notes: {msg}"
        sub = "Request for tutor"

        sendMail(sub, mesg)

    return redirect('home')


def joinUs(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        tel = request.POST['tel']
        nic = request.POST['nic']
        add = request.POST['address']
        pas = request.POST['password']
        edu = request.POST['edu']
        inst = request.POST['inst']
        exp = request.POST['exp']
        img = request.FILES.get('pic')
        about = request.POST["about"]
        ach = request.POST["ach"]
        sub = request.POST["sub"]
        #         math = request.POST['math']
        #         sci = request.POST['sci']
        # #        hist = request.POST['hist']
        #         geo = request.POST['geo']
        #         busn = request.POST['busn']
        #         arts = request.POST['arts']

        b = ""
        for i in pas:
            x = ord(i) * 47
            b += bin(x)
        pas = b

        # sub = [math, sci, hist, geo, busn, arts]

        tu = Tutor
        obj = tu(name=name, nic=nic, email=email, phone=tel, add=add, pas=pas, qua=edu, inst=inst, exp=exp, ach=ach,
                 sub=sub)

        if img:
            obj.pic = img
        # else:
        #     obj.pic="static/images/profile.jpg"
        if about:
            obj.about = about
        else:
            obj.about == "--"

        # mesg = f"Name: {name} \nPhone: {tel} \nEmail: {email} \nNIC#: {nic} \nAddress: {add} \nAbout: {about} \nEducation: {edu}, {inst} \nExperience: {exp} "

        # obj_sub = [obj.math, obj.sci, obj.arts, obj.geo, obj.hist, obj.bus]

        # for i in range(len(sub)):
        #     if sub[i] == "checked":
        #         obj_sub[i] = True
        #     else:
        #         obj_sub[i] = False

        obj.approval = 0
        obj.save()

        mesg = (
            f"Name: {name} \nPhone: {tel} \nEmail: {email} \nNIC#: {nic} \nAddress: {add} \nAbout: {about} \nEducation: {edu}, {inst} \nExperience: {exp}"
            f"Image {obj.pic.url}")

        sub = "Tutor Registration"

        sendMail(sub,mesg)



        return redirect('login')
    else:
        return render(request, "joinUs.html")


def logIn(request):
    if request.method == "POST":
        ph = request.POST['tel']
        password = request.POST['password']

        obj = Tutor.objects.filter(phone=ph)
        if len(obj) == 1:
            pas = obj[0].pas
            pas = pas.split('0b')
            del pas[0]
            _pas = ""
            for i in pas:
                _pas += chr(int(int(i, 2) / 47))

            if _pas == password:
                request.session['user_logged'] = True
                request.session['user'] = obj[0].nic
                print(request.session['user'])
                # print(request.session['user_logged'])
                return redirect('profile')
            else:
                msg.error(request, "incorrect password")
                return redirect("login")

        else:
            msg.error(request, "No such phone number is registered")
            return redirect('login')

    else:
        return render(request, "login.html")


def profile(request):
    if request.session.has_key('user_logged'):
        try:
            obj1 = Tutor.objects.get(nic=request.session['user'])
            obj2 = ContactUS.objects.all()
            return render(request, "profile.html", {"d": obj1, "data": obj2})

        except Exception as e:
            print(e)
            msg.error(request, "server issue occurred please try again")
            return redirect('login')
    else:
        return redirect('login')


def logOut(request):
    del request.session['user_logged']
    del request.session['user']
    return redirect('login')


def update(request):
    obj = Tutor.objects.get(nic=request.session['user'])
    if request.method == "POST":
        obj.name = request.POST['name']
        obj.email = request.POST['email']
        obj.phone = request.POST['tel']
        obj.add = request.POST['address']
        pas = request.POST['password']
        obj.qua = request.POST['edu']
        obj.inst = request.POST['inst']
        obj.exp = request.POST['exp']
        img = request.FILES.get('pic')
        obj.about = request.POST["about"]
        obj.ach = request.POST["ach"]
        obj.sub = request.POST["sub"]

        # obj.update(name=name, email=email, phone=tel, add=add, qua=edu, inst=inst, exp=exp,
        #            ach=ach, sub=sub, about=about)

        if img:
            obj.pic = img

        if pas:
            b = ""
            for i in pas:
                x = ord(i) * 47
                b += bin(x)
            pas = b
            obj.pas = pas

        obj.save()

        try:

            mesg = (f"Name: {obj.name} \nPhone: {obj.phone} \nEmail: {obj.email} \nNIC#: {obj.nic} \nAddress: {obj.add} \nAbout: {obj.about} \nEducation: {obj.qua}, {obj.inst} \nExperience: {obj.exp} /"
                f"Image {obj.pic.url}")
        except Exception as e:
            print(e)
            mesg=f"ERROR! {e}"

        sub = "Tutor Profile Update"

        sendMail(sub, mesg)

        return redirect('profile')
    else:

        obj = Tutor.objects.get(nic=request.session['user'])
        return render(request, "update.html", {"d": obj})


def yourReq(request):
    obj = TutorApplied.objects.filter(tutor=request.session['user'])
    data = []
    # print(obj[0].tution.tuID)
    # return render(request, "youReq.html")
    for d in obj:
        data.append(d.tution)
        print(d.tution.tuID)
    return render(request, "youReq.html", {"data": data})


def apply(request, id):
    ta = TutorApplied()
    ta.tutor = Tutor.objects.get(nic=request.session['user'])
    ta.tution = ContactUS.objects.get(tuID=id)
    ta.approval = 0
    ta.save()
    try:
        mesg= (f"Name {ta.tutor.name} number {ta.tutor.phone} Apply for {ta.tution.tuID} Education {ta.tutor.qua} {ta.tutor.inst} \n Client Name {ta.tution.name} Address {ta.tution.add} /"
               f"\n Client Number {ta.tution.phone} Fees {ta.tution.fee}")

    except Exception as  e:

        print(e)
        mesg = "ERROR!"

    sendMail("Tutor Applied", mesg)

    return redirect('profile')


def sendMail(sub, mesg):
    try:
        send_mail(sub, mesg, "owa3sali@gmail.com", ["owaisaliarshad@gmail.com"])
        return True
    except Exception as e:
        print(e)
        return False

# def send_whatsapp_message(to, body, media_url):
#     account_sid = 'AC51710f429903daa7631cc60fae01952e'
#     auth_token = '2a213fd6943a1e360234383d672d8ab1'
#     client = Client(account_sid, auth_token)
#     message = client.messages.create(
#         from_='whatsapp:+14155238886',  # Twilio's WhatsApp number
#         body=body,
#         media_url=media_url,
#         to=f'whatsapp:{to}'
#     )
#     return message.sid
