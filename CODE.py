function sortReturnedBooks(books)
  for i from 1 to len(books)-1:
     cur=books[i]
     j=i-1
     while j>=0 and compare(cur,books[j]) is true:
        books[j+1]=books[j]
     books[j+1]=cur
  return books
function compare(a,b)
 if a.shelfnumber<b.shelfnumber:
     return true
else if a.shelfnumber==b.shelfnumber and a.returnorder<b.returnorder:
     return true
else:
    return false
