import hashlib

def sha256_hash(input_string):
    return hashlib.sha256(input_string.encode()).hexdigest()

input1 = '''
This is the secret confession of Richard Buckland
to be revealed by anonymous email if I should
mysteriously vanish.  I have left the last few hex
digits of the SHA256 hash of this message with my
trusted solicitor, Dennis Denuto, which will verify
that this is indeed my intended and unaltered
confession written by me Richard Buckland.

Dennis has not seen this confession he has only seen
the last few digits of the hash.  I have also sent copies
of the last few digits to my bank manager and to my priest
Father Brown.

On the 10th of February I saw Mark Zukerberg peeping
through my window and recording my private and personal
conversation with my friend.

I confronted him and he was very embarrassed.  He
promised to pay me $1 million a year if I would stay
silent and not tell anyone I had seen him do this.  I
agreed but now I worry that it would be cheaper for him
to make me vanish than to keep paying me.'''

input2 = '''This is the secret confession of Richard Buckland
to be revealed by anonymous email if I should
mysteriously vanish.  I have left the last few hex
digits of the SHA256 hash of this message with my
trusted solicitor, Dennis Denuto, which will verify
that this is indeed my intended and unaltered
confession written by me Richard Buckland.

Dennis has not seen this confession he has only seen
the last few digits of the hash.  I have also sent copies
of the last few digits to my bank manager and to my priest
Father Brown.

On the 10th of February I saw Mark Zukerberg near my
house and we struck up a conversation.  He explained all
the things he was doing to ensure that Facebook respects
privacy - both of its users and of others.  It was very
impressive.

I feel awful that I have been criticising Facebook publicly
for so long.  I apologised to him in our conversation and
now I want to confess to the world that actually Facebook
has more than enough privacy features, and that the reason
I spend so much time criticising Facebook is that I am
envious of Mark and wish I was a clever and smart and wise
as he is.  I feel so bad for having been so mean to him for
so many years that I am considering retreating to the outback.
I may well cut off all contact with the world and live as a
hermit from now on.  So do not worry if I vanish it is just
that I feel so guilty that I have been so unfair to Facebook.'''

hash1 = sha256_hash(input1)
counter = 0
while True:
    modified_input2 = input2 + str(counter)
    hash2 = sha256_hash(modified_input2)
    
    if hash1[-2:] == hash2[-2:]:
        break
    
    counter +=1

print(f"Original Hash 1: {hash1}")
print(f"\n \n Modified Input 2: '{modified_input2}'")
print(f"Hash of Modified Input 2: {hash2}")