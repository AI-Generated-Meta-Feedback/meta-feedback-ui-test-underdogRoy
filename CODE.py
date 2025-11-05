function sortReturnedBooks(books)
  for i from 1 to len(books)-1:
     cur=books[i]
     j=i-1
     while j>=0 and compare(cur,books[j]) is true:
        books[j+1]=books[j]
     books[j+1]=cur
  return books
function compare(a,b)
 if a.shelfNumber<b.shelfNumber:
     return true
else if a.shelfNumber==b.shelfNumber and a.returnOrder<b.returnOrder:
     return true
else:
    return false