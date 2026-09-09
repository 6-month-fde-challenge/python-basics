"""
demo_assets.py - real bytes for the demo files
==============================================
The first version of the demo wrote `photo.jpg` by putting the words "a
photograph" into a text file. The organizer filed it into Images/ quite
happily - and then nothing could open it, because a .jpg that is not
JPEG data is not a picture.

So this module holds the real thing:

    .jpg .png .gif    decoded from the base64 below - actual images
    .pdf              assembled byte by byte
    .wav              written with the standard `wave` module
    .zip              written with the standard `zipfile` module

The base64 keeps this file plain text and needs no third-party library
to decode. `.docx`, `.mp3` and `.mp4` are left out of the demo entirely,
because a valid file of those types cannot be made from the standard
library - and a stub that sorts perfectly but will not open is the exact
problem this file exists to fix.

Nothing here is part of the organizer package. It only invents files for
the package to sort.
"""
import base64
import io
import math
import struct
import wave
import zipfile


# --------------------------------------------------------------- images
# Real encoded images, held as base64 so this file stays plain text.
# Turn any of them into file bytes with image_bytes() below.

# 240x160 JPEG - a sky, two hills and a sun
PHOTO_JPEG = """
/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAA4KCw0LCQ4NDA0QDw4RFiQXFhQUFiwgIRokNC43
NjMuMjI6QVNGOj1OPjIySGJJTlZYXV5dOEVmbWVabFNbXVn/2wBDAQ8QEBYTFioXFypZOzI7
WVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVn/wAAR
CACgAPADASIAAhEBAxEB/8QAGgABAQEBAQEBAAAAAAAAAAAAAAMCBQQGAf/EADMQAAICAgAC
CAQFBQEBAAAAAAARAQIDEgQhBRMUMUFRYZEWZKPhIjJCgbEjcaHB0aLw/8QAGQEBAAMBAQAA
AAAAAAAAAAAAAAECAwUE/8QAIREBAAMAAgMBAAMBAAAAAAAAAAECEQMSBBMhMUFRYXH/2gAM
AwEAAhEDEQA/ANajUogjs65WJ6jUoghpieo1KIIaYnqNSiCGmJ6jUoghpieo1KIIaYnqNSiC
GmJ6jUoghpieo1KIIaYnqNSiCGmJ6jUoghpieo1KIIaYnqNSiCGmJ6jUoghpieo1KIIaYogi
mo1MtWxNBFNRqNMTQRTUajTE0EU1Go0xNBFNRqNMTQRTUajTE0EU1Go0xNBFNRqNMTQRTUaj
TE0EU1Go0xNBFNT1dH8H2nP+KP6dOdua/tBS/JFKza35C1aTachjg+jsvFK35MXP8cx/EHVx
dD8LSv44tknzmV7I6ERFYiKxERHKIjwBwuXzeXkn5OR/jp8fjUrH2Nl4MnRHCXqq0tSfOtp/
2zmcX0Vl4eu9J62kQ7TEKY/Y+iBHF5vLxz+7H+l/HpaPzHx6COn0pwUYMkZcdYjHflMeUng1
O7xcsclYtVzL0mluspoIpqNTTVcU1GpRBGWrYnqNSiCGmJ6jUoghpieo1KIIaYnqNRmvGLHN
55+UeZz68TkjL1ky33x4IrPJEL145tGw6Go1NUmL0i1e6YZpFuymJ6jUoghpieo1KIIaYnqN
SiCGmJ6jUoghpiep2+isUU4Tbk7zM937f/f3OQjs9G2ieDrEfpmYn+f9nh86Z9Xz+3p8WI7v
WADjOkAADz8fjjLweSJXKNoleR8/qfRcZaKcJlmfGsx78jgo6/gTPSf+uf5cR2hPUalEEdDX
kxRBG9RqZatjCCN6jUaYwgjeo1GmMIxlvXFSb3lRH+St5rjpNrzEVjvk4vFcRPEZdkqxyiCs
2xelO0s581s99rco8I8iQBm9cRnyF+G4icFvOk98HWpNb1i1ZdZ7pOEerguJjBea3/Jbv9PU
tW2fGXJx79h1UEbiImImJcT3TA1NNebGEEb1Go0xhH5KrEzMqIN2VazNpUQeLLlnJPlWO6CJ
ti9KdpXx3rka5THgUR4YmazExKmD24ckZY8rR3wRF1uTj6/YfqPVwGaMOWa2UVv3zPgQ1GpF
6xes1lStprOw7oObw3F2xRFLxtSO7zg9tOJxXjleI9Lcjj8nBek/jpU5q2hUE7cRirDnJX9p
Z5M/GzaNcUTWJjnM95FOC95+QW5a1/ZY6SzReYxVUxWXM+vkeFG9RqdjipHHWKw517Te2ywg
jeo1NNUxRBFEEZatiaCKIIaYmhKrEzMxERzmZKSqxMzMREc5mfA4fH8dPETOPG4xR/6GrVpN
pS4zircTfk4xx3V/3J5gCr1RERGQAAJAAB7eA4ucN4x3l47T4/p+x2UfMnT6O4/RYc0/g7q2
nw9J9CdY8lN+w6aM5LVx0m1p5FMl64qTa8qP5OXmzWzXduUeEeROs6U7GXLbLZzyjwgmAVem
Iz8D9iZiXEzE+cH4Al7+GzxljW3K/wDJdHJiZiXEqYOjwvERljW3K8f5J1578efYVQRRBE6y
xNBFEENMTQRRBDTE0EUQQ0xTUalNRqY6tieo1KanF6X4+d7cNilRHK9onv8AQmJ1MV2UulOO
rm/o4ZdIn8Von80/8OYAXemIyMgAASAAAAABqtZvZQfuOk3so/eT10pWkKsAaibdXSlrTaKQ
oYAAAAAAAAiZiYmJUwAB1OE4mM0aX5ZI/wAnq1ODEzExMSpjuk6fA8ZusWWfxfptPj6FZY3p
/MPXqNSmo1K6yxPUalNRqNMT1GpTUajTHF+I/lfqfYfEfyv1PsfPsM8ney+O3xHT98uGaY8X
VWn9UWcr05HK6yPUiwy0ctoWic/Fusj1HWR6kWGT7rJ7yt1keo6yPUiwx7rHeVusj1HWR6kW
GPdY7yt1keo6yviyLDHusd5e6vFYqVUVt7QfvbMflb2PAwx7rHeXv7Zj8rew7Zj8rex4GGPd
Y7y9/bMflb2HbMflb2PAwx7rHeXv7Zj8rew7Zj8rex4GGPdY7y9/bMflb2HbMflb2PAwx7rH
eXv7Zj8rew7Zj8rex4GGPdY7y7uPp+ceOK2wzlmP1TZf9N/Efyv1PsfPsMrN7KPoPiP5X6n2
HxH8r9T7Hz7DI72MfQfEfyv1PsPiP5X6n2Pn2GO9jGGGYYZCW2GYYYG2GYYYG2GYYYG2GYYY
G2GYYYG2GYYYG2GYYYG2GYYYG2GYYYG2GYYYG2GYYYG2GYYYG2GYYYG2GYYYGGGYYZKW2GYY
YG2GYYYG2GYYYG2GYYYG2GYYYG2GYYYG2GYYYG2GYYYG2GYYYG2GYYYG2GYYYG2GYYYG2GYY
YG2GYYYGGGYYZZLbDMMMDbDMMMDbDMMMDbDMMMDbDMMMDbDMMMDbDMMMDbDMMMDbDMMMDbDM
MMDbDMMMDbDMMMDbDMMMDbDMMMD/2Q==
"""

# 260x170 PNG - a mock code window with a title bar
SCREENSHOT_PNG = """
iVBORw0KGgoAAAANSUhEUgAAAQQAAACqCAIAAADEC6Z3AAACa0lEQVR42u3dMS9DURiA4VNp
YjEbDSaDiMEgFokIBoPJ5jd0MiAMBIOpv8FmMliISGxGMfkBBulssdmaxun5VKTtrTzP1ns7
HefN1+bGaW1haSMBKY1ZAhADiAHEAGIAMUDP6j2+73Z+svPl+nMrfv/j6Xjny+WDz/j9cxcT
nS9fdj/8bajiZPhWQtcrQQldrwQldL0Cw4+htO9L10v7vnS9tO/1QLViiCdAfjeeAPndeMfr
AV+gQQwgBhADjEgM8fOE/G78PCG/Gz9P8LSBak2GUg+l66UeStdLO14JVPFjUr7v44mR7/t4
YuT7XgkMXs1/uoEv0CAGEAOIAX5Wb72/WQUwGUAMIAYQA4gBxABiADGAGEAMIAYQA4gBxABi
ADFAqu6PlbStXs5YtVF3v/NqEUwGEAOIAcQAYgAxgBhADCAGEAP0S21qetYqgMkAYgAxgBhA
DCAGEAOIAcQAYoA0tNMxFvevrBr98HS2bTKAj0kgBhADiAHEAGIAMYAYQAyQnI4BJgOIAcQA
YgAxgBhADCAGQAwgBkh/Ox3j4e7Iqg3GytqxRTAZQAwgBhADiAHEAGIAMYAYQAyQnI4BJgOI
AcQAYgAxgBhADCAGEAOIAZLTMX7jurFp1Wjbat6YDOBjEogBxABiADGAGEAMIAZLAGKA5HQM
MBlADCAGEAOIAcQAYgAxgBhADJAqczrG4V7DqgVOzpsWwWQAMYAYQAwgBhADiAHEAGIAMUBy
OgZgMoAYQAwgBhADiAHEAGIAMYAYQAwgBhADiAHEAGIAMYAYQAwgBhADiAHEAGIAMYAYQAwg
BhADiAH+oS/lc1WaxeMiRgAAAABJRU5ErkJggg==
"""

# 140x140 GIF - a play button on a navy square
LOGO_GIF = """
R0lGODdhjACMAIEAAA0bPv/WCgAAAAAAACwAAAAAjACMAEAI/wABCBxIsKDBgwgTKlzIsKHD
hxAjSpxIsaLFixgzatzIsaPHACBDihxJsqTJkyM9qpSIsqXLlzBdruwYEyaAmjhzppwJUafN
hT6DmuSZUOjPikZzEh2Y9OjKpiSXQpW5lGnTqlNR0sxasqpVriJZgnXqleDYg2ODlo2Ytu3L
tSrdQoVL92HSunjz6t3Lt6/fv4ADCx5MNC1hrHLnHgaauHFUwWcNOiYLV67YyWHLNt7qFnHi
tYp5Oi4M1utni5gD1G3LMPVQv1lvuqa6+Ovsu7VR31adu7fv38CDCx9OvLjx48iTX26p3HTq
5j13a4UuW7pP4ta59s7eGbJ229x58/81jDC8+NWsHVqne3ribM3tL052bjkuedLxZ34XvZm9
UKn94Rcaf/V9dB+A3WE0GmgJLrdgZek1tF5eBxZk3l/7VRfeYeZlWFuH/xkHInPUgcddidHl
h+KKLLbo4oswxijjjDTWaOONOOao44489ujjjzriBqRkAQa5W40jujjiY9AteVJyTlLmW5Q4
AUfldbldqRaHWho12HdLAhaZidn1VSGZR+oVYXkn4tWgQmX6t2Zr0sl5poTvMfgmW8/Bt6d7
DyL4J1IqPlWofINyVqCBY+pXpKGxCZgoo0I6eiiBW2I6KaSZWrqopCFqOqd9kYLaqKKlmloa
qqsKOqpun4pf2iqsl5L6ql19+nknna6htyubt1H4q4V1qnkqkRPudaxAF8LmIYiBgZnkl11i
yWW1NU2JLW2/bfsadt6C1Fy1LDop44Y49jrksEMSy2278MYr77z01mvvvfjmq29EAQEAOw==
"""

# The two JPEGs that are placed in organized/Images/ BEFORE the run, so
# the duplicate-name branch has something real to collide with.
# 240x160 JPEG - a warm sunset, already filed
PHOTO_ALT1_JPEG = """
/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAA4KCw0LCQ4NDA0QDw4RFiQXFhQUFiwgIRokNC43
NjMuMjI6QVNGOj1OPjIySGJJTlZYXV5dOEVmbWVabFNbXVn/2wBDAQ8QEBYTFioXFypZOzI7
WVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVn/wAAR
CACgAPADASIAAhEBAxEB/8QAGgABAQADAQEAAAAAAAAAAAAAAAIBBAYDBf/EAC8QAQEAAgIA
BQIEBAcAAAAAAAARAQIDBAUSITFBE1EiYYHBFDJCsVJxkaHR8PH/xAAZAQEBAQEBAQAAAAAA
AAAAAAAAAQIDBAX/xAAYEQEBAQEBAAAAAAAAAAAAAAAAARECMf/aAAwDAQACEQMRAD8A9qVN
K8D6yqVNKCqVNKCqVNKCqVNKCqVNKCqVNKCqVNKCqVNKCqVNKCqVNKCqVNKCqVNKCqVNKCqV
NKDFKmlVFUqaUFUqaUFUqaUFUqaUFUqaUFUqaUFUqaUFUqaUFUqaUFUrGuM7bY11xnOc5mMY
+W1x+G9zk1uvBtjFn4pr/cNa1K2OTw7ucU83X3zf8P4v7NWhqqVNKCqVNKCqVNKCaVNKIqlT
SgqlTSgqlTSgqlTSgqlTSgqlTSgqlTSgqlTSgqtno9Pk7vN5OP01x/Ntn21w1dcZ22xrrjOd
s5mMY98ux6PWx1OppxYnmxi7Zx85+Ss9dYz1enwdTWcOmMZkztn1zn9XuDLiNTueH8Hb1znb
XGvJnHpyY9/1+7bAlxxnZ6/J1ebPFy4m2P8ATOPvh5V1Xi/U/iult5cXk4/xa+nrn74/78xy
dajtz1sVSppRpVKmlBilTSqiqVNKCqVNKCqVNKCqVNKCqVNKCqVNKCqVNKCqVNKDe8J48cvi
fBrtnMxt5vT8sX9nXuN8K5fpeJ9faW7eX3+/p+7sma59+gDLAAA4js6Y4e1zceuc5103zri+
/pl27hufl+t2OTlnl8+2dpfa5ajfCaVNK06KpU0oJpU0qoqlTSgqlTSgqlTSgqlTSgqlTSgq
lTSgqlTSgqlTSgquz8K7uO709ds7Yzy64nJj5v3/AF93FV7dXtcvU59eXh2m2PfHxnH2ylms
2a7sfP6PjHV7k1830uXP9G/zn8s/Pv8A5/k+gw5gPld/xzr9fXbXg2xzcs9PL664z+ef+P8A
YM1nx7u46/Tzw67Y+ry4k+ca/Of2/wDHKVnm5uTn5duTl2ztvtm5zlFbkx1kxVKmlVVUqaUG
KVNKIqlTSgqlTSgqlTSgqlTSgqlTSgqlTSgqlTSgqlTSgqlTSgqvXi7XPw6514ufl49c5s13
zjFeFKI9uXsc3PPrcvJyT28+2cx51NKCqVNKKqlTSgqlTSgmlTSqyqlTSgqlTSgqlTSgqlTS
gqlTSgqlTSgqlTSgqlTSgqlTSgqlTSgqlTSgqlTSgqlTSgqlTSgxSppVRVKmlBVKmlBVKmlB
VKmlBVKmlBVKmlBVKmlBVKmlBVKmlBVKmlBVKmlBVKmlBVKmlBVKmlBNKmlEVSppQVSppQVS
ppQVSppQVSppQVSppQVSppQVSppQVSppQVSppQVSppQVSppQVSppQVSppQYpU0qoqlTSgqlT
SgqlTSgqlTSgqlTSgqlTSgqlTSgqlTSgqlTSgqlTSgqlTSgqlTSgqlTSgqlTSg//2Q==
"""

# 240x160 JPEG - a dusk scene, already filed
PHOTO_ALT2_JPEG = """
/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAA4KCw0LCQ4NDA0QDw4RFiQXFhQUFiwgIRokNC43
NjMuMjI6QVNGOj1OPjIySGJJTlZYXV5dOEVmbWVabFNbXVn/2wBDAQ8QEBYTFioXFypZOzI7
WVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVlZWVn/wAAR
CACgAPADASIAAhEBAxEB/8QAGwABAQEAAwEBAAAAAAAAAAAAAAECAwQHBQb/xAAtEAEBAAIB
AwIFAwMFAAAAAAAAEQECAwQFEiExE0FRYYEGFCKRscEycdHw8f/EABkBAQADAQEAAAAAAAAA
AAAAAAABAwUCBP/EACARAQADAAICAgMAAAAAAAAAAAABAhEDMQQTEiFBYXH/2gAMAwEAAhED
EQA/AOhSpStF0tKlKC0qUoLSpSgtKlKC0qUoLSpSgtKlKC0qUoLSpSgtKlKC0qUoLSpSgtKl
KC0qUoIIIFEAUQBRAFEAUQBRAFEAUQBRAFDXXbfbGuuM7bbZmMYxc5y73F2buHNrnbXpd8Yx
mfzzjXP9Mxza1a9ynNdEdzm7R3Dhnn0vJm+3hjz/ALV0iLRbqTMUQdIUQBRAGaVKVAtKlKC0
qUoLSpSgtKlKC0qUoLSpSgtKlKC0qUoLXc7b2/m7j1Hw+L01x67759tcf8/Z09ddt9sa6Yzt
ttmYxjFznL0HtnR69B0PHwYnljF3zj57Z9/+/SPP5HN66/Xcuq12Tou3dL0Os4OLGNpM759d
s/n8e3s7QMmZm07K8dDuPael6/XbO+mNObOPTl1x637/AF9vm74VtNZ2CY1531nS83RdRtw8
+s2x7Z+W2Prj7OCv3Hfuh/e9u28NbzcX89Jj1z9cfnHy+sfhq1+Dl9ld/Ki1claVKVe5WlSl
BBmlQNDNKDQzSg0M0oNDNKDQzSg0M0oNDNKDQzSg+j2Li15u89LrtnOMY28vT664znH9n755
/wBk5vgd46Xfx8rv4Sz/AFfx/wAvQGb5m/OP4u4+gB4lgAA846zi14Os5+HTOc68fJtrjOfe
YzHo7zXqub9x1XNzePj8TfbeWy5r3+Fuyq5GBmlaCpoZpQQQBRAFEAUQBRAFEAUQBRAFEAV6
B2XuGvcOg03ztjPNpjx5cfPGfr+ff/x585+i6zm6Hqdefg28d8e+M+22Ppn7KOfi9lf26rbJ
elD5fbu/dH1/jp5/B5s+nw+T0ufT2z7Z9c/7/Z9Rk2rNZy0L4negHxO5fqPpOl0206bbHUc8
9PH10xn75+f4+nyTSlrzlYJmI7X9Tdw16XoNun02x8bnx4z541+ef8fn7PxLXPz8nUc2/Nzb
535N83O2fmw1uHijjrjz2tsqILkKIAzSpSoFpUpQWlSlBaVKUFpUpQWlSlBaVKUFpUpQWlSl
BaVKUFrn4es6np9M6cHUc3FrnNzjTfOMX8OvSomN7HNz9Vz9R4/H5+Xl8fbz3ztP6uKpSkfX
QtKlKkWlSlBaVKUEGaVCGhmlBoZpQaGaUGhmlBoZpQaGaUGhmlBoZpQaGaUGhmlBoZpQaGaU
GhmlBoZpQQQQKIAogCiAKIAogCiAKIAogCiAKIAogCiAKIAogDNKlKC0qUoLSpSgtKlKC0qU
oLSpSgtKlKC0qUoLSpSgtKlKC0qUoLSpSgtKlKC0qUoLSpSggyIGhkBoZAaGQGhkBoZAaGQG
hkBoZAaGQGhkBoZAaGQGhkBoZAf/2Q==
"""


def image_bytes(blob):
    """
    Decode one of the base64 constants above into real file bytes.

    The constants are written across many lines for readability, so the
    whitespace is stripped out before decoding - base64 itself has no
    concept of a line break.
    """
    return base64.b64decode("".join(blob.split()))


# ------------------------------------------------------------------ PDF
def pdf_bytes(title, lines):
    """
    Build a one-page PDF. It really opens in a PDF viewer.

    A PDF is numbered objects followed by an `xref` table of BYTE
    OFFSETS into itself - which is why the offsets are recorded as each
    object is written rather than worked out in advance.
    """
    def escape(text):
        # ( ) and backslash are syntax inside a PDF string literal.
        return (text.replace(chr(92), chr(92) * 2)
                    .replace("(", chr(92) + "(")
                    .replace(")", chr(92) + ")"))

    commands = ["BT", "/F1 20 Tf", "40 200 Td", f"({escape(title)}) Tj", "ET"]
    y = 165
    for line in lines:
        commands += ["BT", "/F1 11 Tf", f"40 {y} Td", f"({escape(line)}) Tj", "ET"]
        y -= 18
    stream = "\n".join(commands).encode("latin-1")

    objects = [
        b"<< /Type /Catalog /Pages 2 0 R >>",
        b"<< /Type /Pages /Kids [3 0 R] /Count 1 >>",
        b"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 420 260] "
        b"/Resources << /Font << /F1 5 0 R >> >> /Contents 4 0 R >>",
        b"<< /Length " + str(len(stream)).encode() + b" >>\nstream\n"
        + stream + b"\nendstream",
        b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica "
        b"/Encoding /WinAnsiEncoding >>",
    ]

    out = bytearray(b"%PDF-1.4\n")
    offsets = []
    for number, body in enumerate(objects, start=1):
        offsets.append(len(out))            # where this object begins
        out += f"{number} 0 obj\n".encode() + body + b"\nendobj\n"

    xref_at = len(out)
    out += f"xref\n0 {len(objects) + 1}\n".encode()
    out += b"0000000000 65535 f \n"         # the mandatory free entry
    for offset in offsets:
        out += f"{offset:010d} 00000 n \n".encode()
    out += (f"trailer\n<< /Size {len(objects) + 1} /Root 1 0 R >>\n"
            f"startxref\n{xref_at}\n%%EOF\n").encode()
    return bytes(out)


# ------------------------------------------------------------------ WAV
def wav_bytes(frequency=440, milliseconds=400, rate=8000, volume=0.35):
    """Build a real, playable WAV file: one short beep."""
    frames = bytearray()
    count = int(rate * milliseconds / 1000)

    for index in range(count):
        # A short fade in and out, so the beep does not click.
        fade = min(1.0, index / 240, (count - index) / 240)
        sample = volume * fade * math.sin(2 * math.pi * frequency * index / rate)
        frames += struct.pack("<h", int(sample * 32767))

    buffer = io.BytesIO()
    with wave.open(buffer, "wb") as handle:
        handle.setnchannels(1)          # mono
        handle.setsampwidth(2)          # 2 bytes = 16-bit
        handle.setframerate(rate)
        handle.writeframes(bytes(frames))
    return buffer.getvalue()


# ------------------------------------------------------------------ ZIP
def zip_bytes(members):
    """Build a real ZIP archive from a {name: text} mapping."""
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w", zipfile.ZIP_DEFLATED) as archive:
        for name, text in members.items():
            archive.writestr(name, text)
    return buffer.getvalue()


# Running this file directly checks that every asset really decodes.
if __name__ == "__main__":
    images = {
        "photo.jpg": PHOTO_JPEG,
        "screenshot.PNG": SCREENSHOT_PNG,
        "logo.gif": LOGO_GIF,
        "photo.jpg (pre-existing)": PHOTO_ALT1_JPEG,
        "photo (1).jpg (pre-existing)": PHOTO_ALT2_JPEG,
    }

    # The first bytes of a file are its "magic number" - the real
    # evidence that it is what its extension claims.
    MAGIC = {b"\xff\xd8\xff": "JPEG", b"\x89PNG": "PNG", b"GIF8": "GIF",
             b"%PDF": "PDF", b"RIFF": "WAV", b"PK\x03\x04": "ZIP"}

    def identify(data):
        for prefix, name in MAGIC.items():
            if data.startswith(prefix):
                return name
        return "unknown"

    print("demo_assets.py self-test")
    print("=" * 58)
    for name, blob in images.items():
        data = image_bytes(blob)
        print(f"   {name:<30} {len(data):>6} bytes  {identify(data)}")

    for name, data in [
        ("report.pdf", pdf_bytes("Report", ["one", "two"])),
        ("beep.wav", wav_bytes()),
        ("backup.zip", zip_bytes({"a.txt": "hello"})),
    ]:
        print(f"   {name:<30} {len(data):>6} bytes  {identify(data)}")
