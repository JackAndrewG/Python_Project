from django.core.exceptions import ValidationError
 
def valid_extension(value):
	print ("Realizando la validación")
	if (not value.name.endswith('.png') and
        not value.name.endswith('.jpeg') and 
        not value.name.endswith('.gif') and
        not value.name.endswith('.bmp') and 
        not value.name.endswith('.jpg')):
		raise ValidationError("Archivos permitidos : .jpg, .jpeg, .png, .gif, .bmp")
