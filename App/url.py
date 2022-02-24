from django.urls import path
from . import views


urlpatterns=[
    path("Register", views.Register, name="Register"),
    path("Login", views.Login, name="Login"),
    path("CompareSentences", views.CompareSentences, name="CompareSentences"),
    path("LetterTestScore", views.LetterTestScore,name="LetterTestScore"),
    path("SentenceTestScore", views.SentenceTestScore,name="SentenceTestScore"),
    path("GetSentenceTestScore", views.GetSentenceTestScore,name="GetSentenceTestScore"),
    path("WordsTestScore", views.WordsTestScore,name="WordsTestScore"),
    path("GetWordsTestScore",views.GetWordsTestScore,name="GetWordsTestScore"),
    path("SetStoryTestScore",views.SetStoryTestScore,name="SetStoryTestScore"),
    path("CompareStories",views.CompareStories,name="CompareStories"),
    path("Retake",views.Retake,name="Retake"),
    path("Resetpaswword",views.Resetpaswword,name="Resetpaswword"),
    path("FetchIntelligenceQsn",views.FetchIntelligenceQsn,name="FetchIntelligenceQsn"),
    path("GetIntelligenceResult",views.GetIntelligenceResult,name="GetIntelligenceResult"),
    path("GetInventoryQuestions",views.GetInventoryQuestions,name="GetInventoryQuestions"),
    path("SendInventoryResult",views.SendInventoryResult,name="SendInventoryResult"),
    path("GetCompletedTest",views.GetCompletedTest,name="GetCompletedTest"),
    path("PosttestletterScore",views.PosttestletterScore,name="PosttestletterScore"),
    path("PostSentenceTestScore",views.PostSentenceTestScore,name="PostSentenceTestScore"),
    path("PostWordsTestScore",views.PostWordsTestScore,name="PostWordsTestScore2"),
    path("PostTestGetWordsTestScore",views.PostTestGetWordsTestScore,name="PostTestGetWordsTestScore"),
    path("PostCompareStories",views.PostCompareStories,name="PostCompareStories"),
    path("Verify/<token>", views.Verify,name="Verify"),
]