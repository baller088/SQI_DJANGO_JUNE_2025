from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from .models import Book, Review
from .forms import ReviewForm

def book_list(request):
    books = Book.objects.all()
    return render(request, 'reviews/book_list.html', {'books': books})

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    reviews = book.reviews.all()
    form = ReviewForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            review = form.save(commit=False)
            review.book = book
            review.save()
            return redirect('book_review:book_detail', pk=book.pk)
    return render(request, 'reviews/book_detail.html',{
        'book': book,
        'reviews': reviews,
        'form': form
    })


def update_review(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    form = ReviewForm(instance=review)
    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect("book_review:book_detail", pk=review.book.pk)
    context = {
        'form' : form,
        'review' : review
    }
    return render(request, "reviews/update_review.html",  context)

def confirm_delete(request, review_pk):
    book = get_object_or_404(Review, pk=review_pk)
    return render(request, "book_review/confirm_delete.html", {"review" : Review})


def delete_book(request, review_pk):
    book = get_object_or_404(Review, pk=review_pk)
    if request.method == "POST":
        Review.delete()
        return redirect("reviews:book_list")
    return redirect("reviews:book_list", book_id=review_pk)