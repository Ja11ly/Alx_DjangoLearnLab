```python
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
# Output: Updated title to 'Nineteen Eighty-Four'
