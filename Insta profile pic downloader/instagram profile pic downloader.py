import instaloader
mod=instaloader.Instaloader()
a=input("enter id: ")
mod.download_profile(a,profile_pic_only=True)