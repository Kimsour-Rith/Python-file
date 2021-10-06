google = {"A", "B","C","D","E", "F","G","H"}
fb = {"I","J","K","L","A","B","C","D","Z","Y","X"}
ms = {"M","N","O","P","Q","J","K","L"}
fb_and_ms = fb.intersection(ms)

print(google-fb)
print(google.difference(fb))
print(google.difference(google.intersection(fb)))

print(fb-google)
print(fb.difference(google))
print(fb.difference(fb.intersection(google)))

print(google,fb_and_ms)
print(google-fb, fb-google)

