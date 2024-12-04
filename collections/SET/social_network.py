users=["rahul","rohith","kohli","rishab","sanju","pandya","siraj"]

rahul_followers=["rohith","kohli","rishab","rahul"]

sanju_followers=["sanju","rohith","kohli"]

mutal_friends=set(rahul_followers).intersection(set(sanju_followers))

follow_sugestions=set(users).difference(rahul_followers)

print(follow_sugestions)
print(mutal_friends)