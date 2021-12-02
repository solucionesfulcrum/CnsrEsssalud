from django.db import models

# Create your models here.

class paciente(models.Model):
    tipo_doc = models.CharField(max_length=40)
    num_doc = models.CharField(max_length=15)
    ape_pat = models.CharField(max_length=40)
    ape_mat = models.CharField(max_length=50)    
    nombres = models.CharField(max_length=50)
    fecha_nac = models.DateField(null=True, blank=True)
    sexo = models.CharField(max_length=10, null=True)
    estado = models.CharField(max_length=5, default=1)

    def __str__(self):
        return (self.nombres+' '+self.ape_pat+' '+self.ape_mat)

class examen(models.Model):
    paciente = models.ForeignKey(paciente, on_delete=models.CASCADE)
    tipo_exam = models.CharField(max_length=50, null=True)
    archivo_exam = models.FileField(upload_to='media/', null=True)
    estado_lectura = models.CharField(max_length=30, null=True)
    estado = models.CharField(max_length=5, default='1')
    fecha_reg = models.DateTimeField(auto_now_add=True)
    user_reg = models.CharField(max_length=40, null=True)
    fecha_mod = models.DateTimeField(null=True)
    user_mod = models.CharField(max_length=50, null=True)
    fecha_eli = models.DateTimeField(null=True)
    user_eli = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.tipo_exam

class archivo(models.Model):
    paciente = models.ForeignKey(paciente, on_delete=models.CASCADE)
    numHisCli = models.CharField(max_length=30, null=True)
    numBalda = models.CharField(max_length=30, null=True)
    estado = models.CharField(max_length=5, default='1')
    user_reg = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.numHisCli

class dependencia(models.Model):
    codDep = models.CharField(max_length=20, unique=True)
    descDep = models.CharField(max_length=50)

    def __str__(self):
        return self.descDep

# Inventario Mantenimiento

class ambiente(models.Model):
    codAmb = models.CharField(max_length=11)
    descAmb = models.CharField(max_length=50)
    dependencia = models.ForeignKey(dependencia, on_delete=models.CASCADE)

    def __str__(self):
        return self.descAmb

class personal(models.Model):
    dniPer = models.CharField(max_length=8, unique=True)
    apePatPer = models.CharField(max_length=50)
    apeMatPer = models.CharField(max_length=50)
    nomPer = models.CharField(max_length=50)
    sexo = models.CharField(max_length=50)
    fecNacPer = models.DateField(null=True)
    codPlaPer = models.CharField(max_length=50)
    regPer = models.CharField(max_length=50)
    cargoPer = models.CharField(max_length=50)
    nivelPer = models.CharField(max_length=50)
    telefoPer = models.CharField(max_length=50)
    correoPer = models.CharField(max_length=50)
    direcPer = models.CharField(max_length=50)
    estPer = models.CharField(max_length=5, default=1)
    dependencia = models.ForeignKey(dependencia, on_delete=models.CASCADE)

    def __str__(self):
        return (self.dniPer + " " + self.apePatPer + " " + self.apeMatPer + " " + self.nomPer)

class bienpat(models.Model):
    codEti = models.CharField(max_length=30, unique=True)
    propBien = models.CharField(max_length=50, default='ESSALUD')
    desBien = models.CharField(max_length=100)    
    serBien = models.CharField(max_length=50)
    modBien = models.CharField(max_length=15)
    marBien = models.CharField(max_length=15)
    situBien = models.CharField(max_length=5, default='B')
    valBien = models.IntegerField(default=0)
    estBien = models.CharField(max_length=5, default=1)
    
    def __str__(self):
        return (self.codEti + " | " + self.desBien)

#Mantenimiento de Maquina

class proveedor(models.Model):
    rucProveedor = models.CharField(max_length=30, unique=True)
    nombreProveedor = models.CharField(max_length=50)
    telefProveedor = models.CharField(max_length=20)
    direcProveedor = models.CharField(max_length=20, null=True)
    estadoProveedor = models.CharField(max_length=5, default=1)

    def __str__(self):
        return self.nombreProveedor

class provMaq(models.Model):
    usobien = models.CharField(max_length=5)
    bienpat = models.ForeignKey(bienpat, on_delete=models.CASCADE)

    def __str__(self):
        return self.usobien

class bienImag(models.Model):
    imagen = models.ImageField(upload_to='fotos/')
    bienpat = models.ForeignKey(bienpat, on_delete=models.CASCADE)

class bienPersonal(models.Model):
    personal = models.ForeignKey(personal, on_delete=models.CASCADE)
    bienpat = models.ForeignKey(bienpat, on_delete=models.CASCADE)

class bienAmbiente(models.Model):
    ambiente = models.ForeignKey(ambiente, on_delete=models.CASCADE)
    bienpat = models.ForeignKey(bienpat, on_delete=models.CASCADE)

class maestro(models.Model):
    codMaestro = models.CharField(max_length=10)
    descripMaestro = models.CharField(max_length=50)
    detalleMaestro = models.CharField(max_length=50)

class incidenciaDsi(models.Model): 
    personal = models.ForeignKey(personal, on_delete=models.CASCADE)
    problema = models.CharField(max_length=200)
    clasiSolu = models.CharField(max_length=50, null=True)
    solucion = models.CharField(max_length=500, null=True)
    estado = models.CharField(max_length=10, default='Pendiente')
    userReg = models.CharField(max_length=20)
    fecha_reg = models.DateTimeField(auto_now=True)
    numTicket = models.CharField(max_length=20)


    
    
