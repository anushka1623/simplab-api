from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
import numpy as np

# import time
# from reportlab.lib.enums import TA_JUSTIFY
# from reportlab.lib.pagesizes import letter
# from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
# from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
# from reportlab.lib.units import inch

# doc = SimpleDocTemplate(
#     "form_letter.pdf",
#     pagesize=letter,
#     rightMargin=72,
#     leftMargin=72,
#     topMargin=72,
#     bottomMargin=18,
# )
# Story = []
# logo = "p.png"
# magName = "Pythonista"
# issueNum = 12
# subPrice = "99.00"
# limitedDate = "03/05/2010"
# freeGift = "tin foil hat"
# formatted_time = time.ctime()
# full_name = "Mike Driscoll"
# address_parts = ["411 State St.", "Marshalltown, IA 50158"]
# im = Image(logo, 2 * inch, 2 * inch)
# Story.append(im)
# styles = getSampleStyleSheet()
# styles.add(ParagraphStyle(name="Justify", alignment=TA_JUSTIFY))
# ptext = '<font size="12">%s</font>' % formatted_time
# Story.append(Paragraph(ptext, styles["Normal"]))
# Story.append(Spacer(1, 12))
# # Create return address
# ptext = '<font size="12">%s</font>' % full_name
# Story.append(Paragraph(ptext, styles["Normal"]))
# for part in address_parts:
#     ptext = '<font size="12">%s</font>' % part.strip()
#     Story.append(Paragraph(ptext, styles["Normal"]))
# Story.append(Spacer(1, 12))
# ptext = '<font size="12">Dear %s:</font>' % full_name.split()[0].strip()
# Story.append(Paragraph(ptext, styles["Normal"]))
# Story.append(Spacer(1, 12))
# ptext = (
#     '<font size="12">We would like to welcome you to our subscriber base for %s Magazine! \
#         You will receive %s issues at the excellent introductory price of $%s. Please respond by\
#         %s to start receiving your subscription and get the following free gift: %s.</font>'
#     % (magName, issueNum, subPrice, limitedDate, freeGift)
# )
# Story.append(Paragraph(ptext, styles["Justify"]))
# Story.append(Spacer(1, 12))
# ptext = '<font size="12">Thank you very much and we look forward to serving you.</font>'
# Story.append(Paragraph(ptext, styles["Justify"]))
# Story.append(Spacer(1, 12))
# ptext = '<font size="12">Sincerely,</font>'
# Story.append(Paragraph(ptext, styles["Normal"]))
# Story.append(Spacer(1, 48))
# ptext = '<font size="12">Ima Sucker</font>'
# Story.append(Paragraph(ptext, styles["Normal"]))
# Story.append(Spacer(1, 12))

# ptext = '<p style="text-decoration:underline">Hello Mayank Meena</p>'
# Story.append(Paragraph(ptext, styles["Normal"]))

# doc.build(Story)


@api_view(["GET"])
def get_user(request, userid):
    if request.method == "GET":
        users = User_Detail.objects.get(user=userid)
        serializedData = User_Detail_Serializer(users)
        return Response(serializedData.data)


@api_view(["POST", "GET"])
def post_user(request):
    if request.method == "GET":
        users = User_Detail.objects.all()
        serializedData = User_Detail_Serializer(users, many=True)
        return Response(serializedData.data)

    if request.method == "POST":
        serialized_user = User_Serializer(data=request.data)
        if serialized_user.is_valid():
            serialized_user.save()
            serialized_user_detail = User_Detail_Serializer(
                data={
                    "user": serialized_user.data["id"],
                    "username": serialized_user.data["username"],
                    "email": serialized_user.data["email"],
                }
            )
            if serialized_user_detail.is_valid():
                serialized_user_detail.save()
            return Response(serialized_user.data["id"])
        return Response(serialized_user.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def auth_user(request, username, password):
    try:
        user = User.objects.get(username=username, password=password)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        user_detail = User_Detail.objects.get(user=user.id)
        serializedData = User_Detail_Serializer(user_detail)
        return Response(serializedData.data)


@api_view(["GET"])
def get_simulations(request):
    if request.method == "GET":
        simulations = Experiment.objects.all()
        serializedData = Experimennt_Serializer(simulations, many=True)
        return Response(serializedData.data)


@api_view(["GET"])
def get_exp_detail(request, exp_id):
    try:
        exp = Experiment.objects.get(pk=exp_id)
    except Experiment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializedData = Experimennt_Serializer(exp)
        return Response(serializedData.data)


@api_view(["POST"])
def post_assignment(request):
    if request.method == "POST":
        serialized_assignment = Assignment_Serializer(data=request.data)
        if serialized_assignment.is_valid():
            serialized_assignment.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(
            serialized_assignment.errors, status=status.HTTP_400_BAD_REQUEST
        )


@api_view(["POST", "GET"])
def post_team(request):
    if request.method == "GET":
        teams = Team.objects.all()
        serializedData = Team_Serializer(teams, many=True)
        return Response(serializedData.data)

    if request.method == "POST":
        serialized_team = Team_Serializer(data=request.data)
        if serialized_team.is_valid():
            serialized_team.save()
            return Response(serialized_team.data["id"])
        return Response(serialized_team.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["PUT"])
def join_team(request, team_id, user_id):
    try:
        team = Team.objects.get(pk=team_id)
        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    except Team.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "PUT":
        team.students.add(user)
        team.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["PUT"])
def update_password(request, user_id, password):
    try:
        user = User.objects.get(pk=user_id, password=password)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "PUT":
        serialized_user = User_Serializer(user, data=request.data)
        if serialized_user.is_valid():
            serialized_user.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serialized_user.errors, status=status.HTTP_204_NO_CONTENT)


@api_view(["GET"])
def get_team_detail(request, team_id):
    if request.method == "GET":
        team = Team.objects.get(pk=team_id)
        serializedData = Team_Serializer(team)
        return Response(serializedData.data)


@api_view(["GET"])
def get_user_teams(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        member_teams = Team_Serializer_Basic(
            user.all_member_teams.all(), many=True
        ).data
        admin_teams = Team_Serializer_Basic(user.team_set.all(), many=True).data
        all_teams = np.concatenate((np.array(admin_teams), np.array(member_teams)))
        return Response(all_teams)


@api_view(["GET"])
def get_user_admin_teams(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        teams = user.team_set.all()
        serializedData = Team_Serializer_Basic(teams, many=True)
        return Response(serializedData.data)


@api_view(["GET"])
def get_student_list(request, team_id):
    try:
        team = Team.objects.get(pk=team_id)
    except Team.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        student_ids = team.students.all()
        array = []
        for x in student_ids:
            student = User_Detail.objects.get(user=x.id)
            serialized_student = User_Detail_Serializer_Basic(student)
            array.append(serialized_student.data)

        return Response(array)


@api_view(["GET"])
def get_all_team_assignments(request, team_id):
    try:
        team = Team.objects.get(pk=team_id)
    except Team.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        assignments = team.all_team_experiments.all()
        serializedData = Assignment_Serializer(assignments, many=True)
        return Response(serializedData.data)


@api_view(["PUT"])
def put_user_detail(request, user_id):
    try:
        user_detail = User_Detail.objects.get(user=user_id)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "PUT":
        serialized_user_detail = User_Detail_Serializer(user_detail, data=request.data)
        if serialized_user_detail.is_valid():
            serialized_user_detail.save()
            return Response(serialized_user_detail.data)
        return Response(
            serialized_user_detail.errors, status=status.HTTP_400_BAD_REQUEST
        )


@api_view(["GET"])
def get_all_assignments(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        teams = user.all_member_teams.all()
        all_assignments = []
        for x in teams:
            s = Assignment_Serializer(x.all_team_experiments.all(), many=True)
            for a in s.data:
                all_assignments.append(a)
        return Response(all_assignments)


@api_view(["GET"])
def getchat(request, teamid):
    try:
        team = Team.objects.get(pk=teamid)
    except Team.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        chats = team.chat_set.all()
        serializedData = Chat_Serializer(chats, many=True)
        return Response(serializedData.data)


@api_view(["POST"])
def post_chat(request):
    if request.method == "POST":
        serialized_chat = Chat_Serializer(data=request.data)
        if serialized_chat.is_valid():
            serialized_chat.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serialized_chat.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
def delete_team(request, teamid):
    try:
        team = Team.objects.get(pk=teamid)
    except Team.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "DELETE":
        team.delete()
        return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
def leave_team(request, teamid, userid):
    try:
        team = Team.objects.get(pk=teamid)
        try:
            user = User.objects.get(pk=userid)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    except Team.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "DELETE":
        if user in team.students.all():
            team.students.remove(user)
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["PUT"])
def add_member(request, teamid, user_email):
    try:
        team = Team.objects.get(pk=teamid)
        try:
            user = User_Detail.objects.get(email=user_email)
        except User_Detail.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    except Team.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "PUT":
        student = User.objects.get(pk=user.pk)
        team.students.add(student)
        return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["PUT"])
def put_assignment_detail(request, assignment_id):
    try:
        assignment = Assignment.objects.get(pk=assignment_id)
    except Assignment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "PUT":
        serialized_assignment = Assignment_Serializer(
            assignment, data=request.data, partial=True
        )
        if serialized_assignment.is_valid():
            serialized_assignment.save()
            return Response(serialized_assignment.data)
        return Response(
            serialized_assignment.errors, status=status.HTTP_400_BAD_REQUEST
        )


@api_view(["POST"])
def create_assignment(request):
   if request.method == "POST":
        serialized_assignment = Assignment_Serializer(data=request.data)
        if serialized_assignment.is_valid():
            serialized_assignment.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(
            serialized_assignment.errors, status=status.HTTP_400_BAD_REQUEST
        )


@api_view(["POST"])
def post_submission(request):
    if request.method == "POST":
        serialized_submission = Ass_Submission_Serializer(data=request.data)
        print(serialized_submission)
        if serialized_submission.is_valid():
            serialized_submission.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(
            serialized_submission.errors, status=status.HTTP_400_BAD_REQUEST
        )


@api_view(["GET"])
def submission_list(request, assignment_id):
    try:
        assignment = Assignment.objects.get(pk=assignment_id)
    except Assignment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        assignment_submissions = assignment.assignmentsubmission_set.all()
        serializedData = Ass_Submission_Serializer(assignment_submissions, many=True)
        return Response(serializedData.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def get_chat_files(request, teamid):
    if request.method == "GET":
        chat_files = Chat.objects.filter(team_id=teamid, is_file=True)
        serializedData = Chat_File_Serializer(chat_files, many=True)
        return Response(serializedData.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
def leave_member(request, teamid, user_name):
    try:
        team = Team.objects.get(pk=teamid)
        try:
            user = User.objects.get(username=user_name)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    except Team.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "DELETE":
        if user in team.students.all():
            team.students.remove(user)
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def get_assignment_detail(request,assignment_id):
    try:
        assignment = Assignment.objects.get(pk = assignment_id)
    except Assignment.DoesNotExist:
        return Response(status= status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializedData =  Assignment_Serializer(assignment)
        return Response(serializedData.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
def post_assignment_submission(request):
    if request.method == "POST":
        serialized_assignment_submission = Ass_Submission_Serializer(data=request.data)
        if serialized_assignment_submission.is_valid():
            serialized_assignment_submission.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(
            serialized_assignment_submission.errors, status=status.HTTP_400_BAD_REQUEST
        ) 
    return Response(status=status.HTTP_400_BAD_REQUEST)
