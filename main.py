from Scraper.reddit import RedditScraper

topic = "minecraft"
scraper = RedditScraper(topic, limit=10)
scraper.scrape_top_posts()
scraper.scrape_comments("https://www.reddit.com/r/Minecraft/comments/hi22zu/hope_this_makes_your_day_better/")

















# import os

# def print_directory_structure(root_dir):
#     for dirpath, dirnames, filenames in os.walk(root_dir):
#         level = dirpath.replace(root_dir, '').count(os.sep)
#         indent = '    ' * level
#         print(f"{indent} {os.path.basename(dirpath)}")
#         subindent = '    ' * (level + 1)
#         for file in filenames:
#             print(f"{subindent} {file}")

# # Example usage
# print_directory_structure("D:\Padhaai Ka Saaman\Coding\React\Demeter")