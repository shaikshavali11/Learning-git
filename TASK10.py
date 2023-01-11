st='python narayana tech house'
ans=""
for i in st:
    if i not in 'aeiouAEIOU':
        ans=ans+i.lower()

    else:
        ans=ans+i.upper()

print(ans)
print(type(ans))

