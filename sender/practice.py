import itchat

itchat.auto_login(hotReload=True)

contact_list = itchat.get_contact()

print(contact_list)

friends_list = itchat.get_friends()

# print(friends_list)

