# নাঈম ১৮ - ইউজার রেজিস্ট্রেশন সিস্টেম

def register_member():
    print("--- নতুন সদস্য নিবন্ধন ---")
    
    # মানুষের তথ্য সংগ্রহ
    name = input("সদস্যের নাম লিখুন: ")
    profession = input("পেশা (যেমন: কৃষক, ড্রাইভার, শ্রমিক): ")
    location = input("গ্রাম বা এলাকার নাম: ")
    
    # তথ্যগুলো একটি ফাইলে সেভ করে রাখা
    try:
        with open("members_list.txt", "a", encoding="utf-8") as file:
            file.write(f"নাম: {name} | পেশা: {profession} | এলাকা: {location}\n")
        
        print(f"\nঅভিনন্দন! {name}-এর তথ্য সফলভাবে সিস্টেমে যোগ করা হয়েছে।")
    except Exception as e:
        print("তথ্য সেভ করতে সমস্যা হয়েছে:", e)

# সিস্টেম চালু করার ফাংশন
def start_system():
    while True:
        print("\n১. নতুন সদস্য যোগ করুন")
        print("২. সিস্টেম থেকে বের হয়ে যান")
        
        choice = input("আপনার পছন্দ (১/২): ")
        
        if choice == '১':
            register_member()
        elif choice == '২':
            print("সিস্টেম বন্ধ হচ্ছে... আসসালামুয়ালাইকুম।")
            break
        else:
            print("সঠিক বাটন চাপুন।")

if __name__ == "__main__":
    start_system()
