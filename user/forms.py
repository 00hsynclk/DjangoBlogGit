from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label= "Kullanıcı Adı")
    password = forms.CharField(label= "Şifre", widget= forms.PasswordInput)



class  RegisterForm(forms.Form):
    username = forms.CharField(max_length= 50, label= "Kullanıcı Adı")
    password = forms.CharField(max_length= 20, label= "Parola", widget= forms.PasswordInput)
    confirm = forms.CharField(max_length= 20, label= "Parolayı Doğrula", widget= forms.PasswordInput)
    
    #Password'u kontol etme
    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")

        #Kontrol kısmı
        if password and confirm and password != confirm:
            raise forms.ValidationError("Parolalar eşleşmiyor.")
        
        values = {
            "username" : username,
            "password" : password
        }

        return values