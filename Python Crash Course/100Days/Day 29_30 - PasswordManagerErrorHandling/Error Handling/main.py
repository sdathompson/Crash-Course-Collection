# Four Key Words for Exceptions

# Try: Something that might cause an exception
# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["key"])
# # Except: Do this if there was an exception
# # Add the Error that pops up in the console
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"That key {error_message} does not exist.")
# # Else: Do this if there were no exception
# else:
#     content = file.read()
#     print(content)
# # Finally: Do this no matter what happens
# finally:
#     # This creates an error even if there isn't one
#     raise TypeError("This is an error that I made up")

# Example
# height = float(input("Height(in m): "))
# weight = int(input("Weight(in kg): "))
#
# bmi = weight / height ** 2
# print(bmi)
#
# if height > 3:
#     raise ValueError("Human Height should not be over 3 meters.")

facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]

def count_likes(posts):
    try:
        total_likes = 0
        for post in posts:
            total_likes = total_likes + post['Likes']
    except KeyError as error_key:
        for post in posts:
            key_get = post.get('Likes', 0)
            if key_get == 0:
                post['Likes'] = 0
    finally:
        print(posts)

count_likes(facebook_posts)
