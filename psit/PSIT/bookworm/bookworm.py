"""BookWorm"""
def bookworm(testing):
    """input number of testing to send the input readingtime and input
    bookcount to do something of booktime. At last print bookcount
    as many book between the reading time."""
    booktime = 0
    bookcount = 0
    list_readingtime = []
    list_ans = []
    for i in range(testing):
        readtime = int(input())
        booknumber = int(input())
        for _ in range(booknumber):
            list_readingtime.append(int(input()))
        list_readingtime.sort()
        for k in range(booknumber):
            booktime += list_readingtime[k]
            if booktime <= readtime:
                bookcount += 1
            elif booktime > readtime:
                break
        list_ans.append(bookcount)
        bookcount = 0
        booktime = 0
        list_readingtime = []
    for i in list_ans:
        print(i)
bookworm(int(input()))
