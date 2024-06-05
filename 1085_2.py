x,y,w,h=map(int,input().split())
distX,distY=x if x<=w/2 else w-x,y if y<=h/2 else h-y
print(distX if distX<distY else distY)