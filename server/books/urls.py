from django.urls import path, re_path
from rest_framework import permissions
from books.views.views import (
    BookListAPIView,
    BookDetailAPIView,
    AuthorListAPIView,
    AuthorDetailAPIView,
    AuthorDeleteAPIView,
    AuthorUpdateAPIView,
    AuthorCreateAPIView,
    BookDeleteAPIView,
    BookUpdateAPIView,
    BookCreateAPIView,
    AuthorBookListAPIView,
    GenreListAPIView,
    GenreBookListAPIView,
)
from books.views.search_views import BookSearchAPIView
from books.views.suggestion_views import BookSuggestionAPIView

from books.views.review_views import (
    BookReviewAPIView,
    BookReviewDetailAPIView,
    BookReviewCreateAPIView,
    BookReviewUpdateAPIView,
    BookReviewDeleteAPIView,
    BookReviewsByBookAPIView,
    BookRatingAPIView,
    BookRatingDetailAPIView,
    BookRatingCreateAPIView,
    BookRatingUpdateAPIView,
    BookRatingDeleteAPIView,
    BookRatingsByBookAPIView,
    UserBookRatingAPIView,
    UserRatingsAPIView, 
    UserReviewsAPIView
)

from books.views.upvote_views import (
    ReviewUpvoteCreateAPIView,
    ReviewUpvoteDeleteAPIView,
    ReviewUpvoteToggleAPIView,
    ReviewUpvoteStatusAPIView,
    ReviewsByUpvotesAPIView,
    TopReviewsAPIView,
    UserUpvotedReviewsAPIView
)

from books.views.vote_views import (
    ReviewVoteCreateAPIView,
    ReviewVoteDeleteAPIView,
    ReviewVoteToggleAPIView,
    ReviewVoteStatusAPIView,
    ReviewsByVotesAPIView,
    UserVotedReviewsAPIView,
    ReviewVoteStatsAPIView
)

from books.views.reading_list_views import (
    ReadingListAPIView,
    ReadingListDetailAPIView,
    ReadingListCreateAPIView,
    ReadingListUpdateAPIView,
    ReadingListDeleteAPIView,
    ReadingListBookOperationsAPIView,
    AdminUserReadingListsAPIView,
)



urlpatterns = [
    # Book endpoints
    path("list/", BookListAPIView.as_view(), name="book-list-api"),
    path("search/", BookSearchAPIView.as_view(), name="book-search-api"),
    path("suggestions/", BookSuggestionAPIView.as_view(), name="book-suggestion-api"),
    path("books/create/", BookCreateAPIView.as_view(), name="book-create"),
    path("books/<str:pk>/", BookDetailAPIView.as_view(), name="book-detail-api"),
    path("books/<str:pk>/update/", BookUpdateAPIView.as_view(), name="book-update"),
    path("books/<str:pk>/delete/", BookDeleteAPIView.as_view(), name="book-delete"),
    
    # Author endpoints
    path("authors/", AuthorListAPIView.as_view(), name="authors-list-api"),
    path("authors/<str:pk>/", AuthorDetailAPIView.as_view(), name="author-detail-api"),
    path("authors/create/", AuthorCreateAPIView.as_view(), name="author-create"),
    path("authors/<str:pk>/update/", AuthorUpdateAPIView.as_view(), name="author-update"),
    path("authors/<str:pk>/delete/", AuthorDeleteAPIView.as_view(), name="author-delete"),
    path("authors/<int:pk>/books/", AuthorBookListAPIView.as_view(), name="author-books-by-id"),
    path("authors/name/<str:name>/books/", AuthorBookListAPIView.as_view(), name="author-books-by-name"),
    
    # Genre endpoints
    path("genres/", GenreListAPIView.as_view(), name="genres-list-api"),
    path("genres/<int:pk>/books/", GenreBookListAPIView.as_view(), name="genre-books-by-id"),
    path("genres/name/<str:name>/books/", GenreBookListAPIView.as_view(), name="genre-books-by-name"),

    # Review API endpoints 
    path("reviews/", BookReviewAPIView.as_view(), name="api-review-list"),
    path("reviews/<str:review_id>/", BookReviewDetailAPIView.as_view(), name="api-review-detail"),
    path("review/create/", BookReviewCreateAPIView.as_view(), name="api-review-create"),
    path("reviews/<str:review_id>/update/", BookReviewUpdateAPIView.as_view(), name="api-review-update"),
    path("reviews/<str:review_id>/delete/", BookReviewDeleteAPIView.as_view(), name="api-review-delete"),
    path("books/<str:book_id>/reviews/", BookReviewsByBookAPIView.as_view(), name="api-book-reviews"),
    
    # Review Upvote API endpoints (backward compatibility)
    path("reviews/<str:review_id>/upvote/", ReviewUpvoteCreateAPIView.as_view(), name="api-review-upvote"),
    path("reviews/<str:review_id>/upvote/remove/", ReviewUpvoteDeleteAPIView.as_view(), name="api-review-upvote-remove"),
    path("reviews/<str:review_id>/upvote/toggle/", ReviewUpvoteToggleAPIView.as_view(), name="api-review-upvote-toggle"),
    path("reviews/<str:review_id>/upvote/status/", ReviewUpvoteStatusAPIView.as_view(), name="api-review-upvote-status"),
    path("reviews/by-upvotes/", ReviewsByUpvotesAPIView.as_view(), name="api-reviews-by-upvotes"),
    path("reviews/top/", TopReviewsAPIView.as_view(), name="api-top-reviews"),
    path("reviews/user/upvoted/", UserUpvotedReviewsAPIView.as_view(), name="api-user-upvoted-reviews"),
    
    # Review Vote API endpoints (upvotes and downvotes)
    path("reviews/<str:review_id>/vote/", ReviewVoteCreateAPIView.as_view(), name="api-review-vote"),
    path("reviews/<str:review_id>/vote/remove/", ReviewVoteDeleteAPIView.as_view(), name="api-review-vote-remove"),
    path("reviews/<str:review_id>/vote/toggle/", ReviewVoteToggleAPIView.as_view(), name="api-review-vote-toggle"),
    path("reviews/<str:review_id>/vote/status/", ReviewVoteStatusAPIView.as_view(), name="api-review-vote-status"),
    path("reviews/<str:review_id>/vote/stats/", ReviewVoteStatsAPIView.as_view(), name="api-review-vote-stats"),
    path("review/by-votes/", ReviewsByVotesAPIView.as_view(), name="api-reviews-by-votes"),
    path("reviews/user/voted/", UserVotedReviewsAPIView.as_view(), name="api-user-voted-reviews"),

    # Rating API endpoints
    path("ratings/", BookRatingAPIView.as_view(), name="api-rating-list"),
    path("ratings/<str:rate_id>/", BookRatingDetailAPIView.as_view(), name="api-rating-detail"),
    path("rating/create/", BookRatingCreateAPIView.as_view(), name="api-rating-create"),
    path("ratings/<str:rate_id>/update/", BookRatingUpdateAPIView.as_view(), name="api-rating-update"),
    path("ratings/<str:rate_id>/delete/", BookRatingDeleteAPIView.as_view(), name="api-rating-delete"),
    path("books/<str:book_id>/ratings/", BookRatingsByBookAPIView.as_view(), name="api-book-ratings"),
    path("books/<str:book_id>/my-rating/", UserBookRatingAPIView.as_view(), name="api-user-book-rating"),
    path('users/<str:user_id>/ratings/', UserRatingsAPIView.as_view(), name='user-ratings'),
    path('users/<int:user_id>/reviews/', UserReviewsAPIView.as_view(), name='user-reviews'),
    
    # Reading List API endpoints
    path("reading-lists/", ReadingListAPIView.as_view(), name="reading-lists-api"),
    path("reading-lists/<int:list_id>/", ReadingListDetailAPIView.as_view(), name="reading-list-detail-api"),
    path("reading-lists/create/", ReadingListCreateAPIView.as_view(), name="reading-list-create-api"),
    path("reading-lists/<int:list_id>/update/", ReadingListUpdateAPIView.as_view(), name="reading-list-update-api"),
    path("reading-lists/<int:list_id>/delete/", ReadingListDeleteAPIView.as_view(), name="reading-list-delete-api"),
    path("reading-lists/books/", ReadingListBookOperationsAPIView.as_view(), name="reading-list-books-api"),
    path("users/<int:user_id>/reading-lists/", AdminUserReadingListsAPIView.as_view(), name="admin-user-reading-lists-api"),
    # path("users/me/reading-lists/", UserReadingListsAPIView.as_view(), name="user-reading-lists-api"),
]
