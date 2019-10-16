from django.shortcuts import render, redirect, get_object_or_404
from .forms import QuestionForm
from .models import Question
# Create your views here.

def index(request):
    questions = Question.objects.all()
    context={
        'questions':questions
    }
    return render(request,'questions/index.html',context)

def create(request):
    # 1. 사용자가 데이터를 입력하기 위해서 GET요청(폼을요청)
    # 6. 올바르지 않은 데이터를 입력하고 POST요청
    # 12. 사용자가 올바른 데이터 입력후 POST입력

    # 7. POST method로 들어오기 때문에 if문 실행
    # 13. POST method로 들어오기 때문에 if문 실행
    if request.method == "POST":
        # 8. 사용자의 데이터를 모델폼에 입력
        # 14. 사용자의 데이터를 모델폼에 입력
        form = QuestionForm(request.POST)
        # 9. 데이터가 올바른지 검증
        # 15. 데이터가 올바른지 검증
        if form.is_valid():
            # 16. 데이터가 검증을 통과 하고 저장
            form.save()
            # 17. 저장 후 메인으로 이동
            return redirect('questions:index')
    # 2. GET method로 들어오기 때문에 else문 실행
    else:
        # 3. 사용자에게 빈 폼을 보여주기 위해서 모델폼을
        #    인스턴스화 한 후 form 변수에 저장
        form = QuestionForm()
    # 4. dict로 만들기
    # 10. 검증을 통과 못했을때, 올바른 데이터 남기고, 다시 폼 보여줌
    context={
        'form':form,
    }
    # 5. form.html 보여주기
    # 11. form.html 보여주기
    return render(request,'questions/form.html',context)

def detail(request,id):
    question = get_object_or_404(Question, id=id)
    context={
        'question':question
    }
    return render(request, 'questions/detail.html',context)