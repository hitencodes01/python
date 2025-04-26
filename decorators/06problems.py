is_logged_in = True

def authorize(func):
    def wrapper(*args , **kwargs):
        if(is_logged_in):
            return func(*args , **kwargs)
        else:
            print("not authorized")
            return None
    return wrapper
@authorize
def view_profile():
    print("profile...data...")
view_profile()

is_logged_in = False
view_profile()