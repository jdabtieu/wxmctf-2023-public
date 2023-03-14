from reportlab.pdfgen import canvas
from qrcode import make
from collections import deque
import io, uuid, random

def generate_qr_pdf(data1,data2, name):
    pdf_file = io.BytesIO()
    pdf = canvas.Canvas(pdf_file)
    qr = make(data1)
    qr.save("temp_wsedxcfvgyhujnoikmljnhugvftvghbgvfcdxfgvbh_1.png")
    pdf.drawImage("temp_wsedxcfvgyhujnoikmljnhugvftvghbgvfcdxfgvbh_1.png", 10, 480, 360, 360)
    qr = make(data2)
    qr.save("temp_wsedxcfvgyhujnoikmljnhugvftvghbgvfcdxfgvbh_2.png")
    pdf.drawImage("temp_wsedxcfvgyhujnoikmljnhugvftvghbgvfcdxfgvbh_2.png", 10, 10, 360, 360)
    pdf.save()
    pdf_file.seek(0)
    with open(f"{name}.pdf", "wb") as f:
        f.write(pdf_file.read())

def generate_other_pdf(data, name):
    pdf_file = io.BytesIO()
    pdf = canvas.Canvas(pdf_file)
    qr = make(data)
    qr.save("temp_wsedxcfvgyhujnoikmljnhugvftvghbgvfcdxfgvbh_X.png")
    pdf.drawImage("temp_wsedxcfvgyhujnoikmljnhugvftvghbgvfcdxfgvbh_X.png", 10, 480, 360, 360)
    pdf.save()
    pdf_file.seek(0)
    with open(f"{name}.pdf", "wb") as f:
        f.write(pdf_file.read())
  
def generate_uuid():
    return str(uuid.uuid4())

endpoints = ['https://pastebin.com/js7yA033', #flag
            'https://youtu.be/dQw4w9WgXcQ',
            'https://www.instagram.com/reel/Cm1pSSXKGaD',
            'https://pastebin.com/u3vUcYzi',
            'https://youtu.be/MtN1YnoL46Q']

domain = 'imgs/' # CHANGE THIS !! <------
flag_given = False

queue = deque([('start',0)])
while len(queue) > 0:
    v = queue.popleft() #v[0] is q'd uuid, v[1] is counter
    uuid1 = generate_uuid()
    uuid2 = generate_uuid()
    if v[1] == 11:
        if flag_given:
            i = random.randint(1,4)
        else:
            i = random.randint(0,4)
            if i == 0:  #technically not guaranteed to get flag, but statistically yes 
                flag_given = True
                print('file with flag:', v[0])
        generate_other_pdf(endpoints[i], v[0])
        print(f"generated: {v[0]} | {endpoints[i]}")
    else:
        generate_qr_pdf(domain+uuid1, domain+uuid2, v[0])
        print(f"generated: {v[0]} | {domain+uuid1}, {domain+uuid2}")
        queue.append((uuid1,v[1]+1))
        queue.append((uuid2,v[1]+1))

assert(flag_given)

#could be cyclic to make it harder
