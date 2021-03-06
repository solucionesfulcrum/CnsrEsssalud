from django.db import models

# Ubicacion usuario

class cas(models.Model):
    codCas = models.CharField(max_length=15, unique=True)
    descripCas = models.CharField(max_length=100)
    tipoCas = models.CharField(max_length=10)

    def __str__(self):
        return (self.descripCas)

# Seguridad
class usuario(models.Model):
    num_doc = models.CharField(max_length=15, unique=True)
    nombre = models.CharField(max_length=50)
    cas = models.ForeignKey(cas, on_delete=models.CASCADE)
    usuario = models.CharField(max_length=15, unique=True)
    clave = models.CharField(max_length=20)
    perfil = models.CharField(max_length=50)

    def __str__(self):
        return (self.usuario)

# Create your models here.
class maestro(models.Model):
    codMaestro = models.CharField(max_length=10)
    descripMaestro = models.CharField(max_length=50)
    detalleMaestro = models.CharField(max_length=50)

    def __str__(self):
        return (self.descripMaestro)

class paciente(models.Model):
    tipo_doc = models.CharField(max_length=40)
    num_doc = models.CharField(max_length=15, unique=True)
    ape_pat = models.CharField(max_length=40)
    ape_mat = models.CharField(max_length=50)    
    nombres = models.CharField(max_length=50)
    fecha_nac = models.DateField(null=True, blank=True)
    sexo = models.CharField(max_length=10, null=True)
    cas = models.ForeignKey(cas, on_delete=models.CASCADE)
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
# Tabla Clinicas     

class presAnemia(models.Model):
    paciente = models.ForeignKey(paciente, on_delete=models.CASCADE)
    fechaPres = models.DateField()
    nomNefro = models.CharField(max_length=30)
    medPres = models.CharField(max_length=30)
    dosisPres = models.IntegerField()
    medHiePres = models.CharField(max_length=30)
    dosisHiePres = models.IntegerField()
    viaAdmPres = models.CharField(max_length=10)
    viaAdmHiePres = models.CharField(max_length=10)
    usuario = models.ForeignKey(usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.nomNefro

class admiAnemia(models.Model):
    presAnemia = models.ForeignKey(presAnemia, on_delete=models.CASCADE)
    fechaAdmi = models.DateField()
    nomEnfer = models.CharField(max_length=30)
    medAdmi = models.CharField(max_length=30)
    dosisAdmi = models.IntegerField()
    medHieAdmi = models.CharField(max_length=30)
    dosisHieAdmi = models.IntegerField()
    viaAdm = models.CharField(max_length=10)
    viaAdmHierro = models.CharField(max_length=10)
    usuario = models.ForeignKey(usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.nomEnfer

class exclusionAnemia(models.Model):
    paciente = models.ForeignKey(paciente, on_delete=models.CASCADE)
    fechaExclu = models.DateField()
    razonExclu = models.CharField(max_length=30)
    ObservaExclu = models.CharField(max_length=30)
    usuario = models.ForeignKey(usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.razonExclu

class movimientoAnemia(models.Model):
    paciente = models.ForeignKey(paciente, on_delete=models.CASCADE)
    fechaMotivo = models.DateField()
    razonMotivo = models.CharField(max_length=30)
    obserMotivo = models.CharField(max_length=30)

    def __str__(self):
        return self.razonMotivo

class nutricion(models.Model):
    paciente = models.ForeignKey(paciente, on_delete=models.CASCADE)
    turno = models.CharField(max_length=30)
    frecuencia = models.CharField(max_length=30)
    fechaIngreso = models.DateField(null=True, blank=True)
    fechaEvaluacion = models.DateField(null=True, blank=True)
    peso = models.CharField(max_length=30)
    talla = models.CharField(max_length=30)
    imc = models.CharField(max_length=30)
    porcentajeCMB = models.CharField(max_length=30)
    porcentajeEPT = models.CharField(max_length=30, null=True, blank=True)
    albSerica = models.CharField(max_length=30)
    ValGlobalSub = models.CharField(max_length=30, null=True, blank=True)
    ingestaCalorica = models.CharField(max_length=60)
    ingestaProteica = models.CharField(max_length=60)
    diagNutricional = models.CharField(max_length=60)
    interveNutricional = models.CharField(max_length=60)
    usuario = models.ForeignKey(usuario, on_delete=models.CASCADE)
    fechaReg = models.DateTimeField(auto_now_add=True)
    pacNuevo = models.BooleanField()

    def __str__(self):
        return self.frecuencia

# Tabla Hospitales (VGS)     

class valGlobalSub(models.Model):
    paciente = models.ForeignKey(paciente, on_delete=models.CASCADE)
    fechaEval = models.DateField()
    ganPerPeso = models.CharField(max_length=15) # Ganancia o perdida de Peso  
    camPesoCorp = models.CharField(max_length=15) # Cambio de peso corporal 
    # Cambios en la dieta, en relaci??n con lo normal 
    duraDieta = models.CharField(max_length=15) # Duraci??n 
    resultDieta = models.CharField(max_length=15) # Resultado
    tipoDieta = models.CharField(max_length=40) # Tipo de Dieta
    sintoGastro = models.CharField(max_length=15) # Sintomas gastrointestinales
    disfuncion = models.CharField(max_length=15) # Capacidad funcional 
    cambioCapFun = models.CharField(max_length=15) # Cambio capacidad Funcional
    # Examen Fisico
    grasaSubcu = models.CharField(max_length=15) # P??rdida de grasa subcut??nea 
    atrofiaMusc = models.CharField(max_length=15) # Atrofia muscular 
    EdemaTobi = models.CharField(max_length=15) # Edema de tobillos
    edemaSacro = models.CharField(max_length=15) # Edema sacro
    ascitis = models.CharField(max_length=15) # Ascitis
    # Diagnostico de Valoracion Global Subjestiva
    resultadoVGS = models.CharField(max_length=25) # Ascitis
    fechaReg = models.DateField()
    userReg = models.CharField(max_length=20)

    def __str__(self):
        return self.resultadoVGS

# Inventario Mantenimiento

class dependencia(models.Model):
    codDep = models.CharField(max_length=20, unique=True)
    descDep = models.CharField(max_length=50)

    def __str__(self):
        return self.descDep


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
        return (self.dniPer + " | " + self.apePatPer + " " + self.apeMatPer + " " + self.nomPer)

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
    bienpat = models.OneToOneField(bienpat, on_delete=models.CASCADE, unique=True)

class bienAmbiente(models.Model):
    ambiente = models.ForeignKey(ambiente, on_delete=models.CASCADE)
    bienpat = models.OneToOneField(bienpat, on_delete=models.CASCADE, unique=True)
    personal = models.ForeignKey(personal, on_delete=models.CASCADE)

class bienHadware(models.Model):
    bienpat = models.ForeignKey(bienpat, on_delete=models.CASCADE)
    procesador = models.CharField(max_length=20)
    numeroIp = models.CharField(max_length=20)
    numeroMac = models.CharField(max_length=20)
    memoriaRam = models.CharField(max_length=20)
    capAlmacenamiento = models.CharField(max_length=20)
    uso = models.CharField(max_length=20)
    condicion = models.CharField(max_length=20)

class bienSoftware(models.Model):
    bienpat = models.ForeignKey(bienpat, on_delete=models.CASCADE)
    sistemaOperativo = models.CharField(max_length=20)
    ofimatica = models.CharField(max_length=20)
    antivirus = models.CharField(max_length=20)

class bienDetalleMonitor(models.Model):
    bienpat = models.ForeignKey(bienpat, on_delete=models.CASCADE)
    pulgadas = models.CharField(max_length=20)

class incidenciaDsi(models.Model): 
    personal = models.ForeignKey(personal, on_delete=models.CASCADE)
    problema = models.CharField(max_length=200)
    clasiSolu = models.CharField(max_length=50, null=True)
    solucion = models.CharField(max_length=500, null=True)
    userReg = models.CharField(max_length=20)
    fecha_reg = models.DateTimeField(auto_now=True)
    numTicket = models.CharField(max_length=20)
    estado = models.ForeignKey(maestro, on_delete=models.CASCADE)

class personalVpnAct(models.Model): 
    personal = models.ForeignKey(personal, on_delete=models.CASCADE)
    ip = models.CharField(max_length=30, null=True, blank=True)
    usuario = models.CharField(max_length=30)
    clave = models.CharField(max_length=30)
    personalAutoriza = models.CharField(max_length=40)
    fechaHabilita = models.DateField(null=True, blank=True)
    fechaInstalacion = models.DateField(null=True, blank=True)
    observacion = models.CharField(max_length=200,null=True, blank=True)
    fecha_reg = models.DateTimeField(auto_now=True)
    dato = models.CharField(max_length=30)

    def __str__(self):
        return self.usuario
    
class personalCertificado(models.Model):
    personal = models.ForeignKey(personal, on_delete=models.CASCADE)
    fechaSolicita = models.DateField()
    tipoCertificado = models.CharField(max_length=30)
    fechaInstalacion = models.DateField(null=True, blank=True)
    perosnalInstala =  models.CharField(max_length=40, null=True, blank=True)
    observacion = models.CharField(max_length=200, null=True, blank=True)
    fecha_reg = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.tipoCertificado
