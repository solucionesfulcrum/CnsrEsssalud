from django.contrib import admin
from Asistencial.models import cas,usuario, paciente, examen, archivo, presAnemia, admiAnemia, exclusionAnemia, movimientoAnemia, bienAmbiente, bienPersonal, bienpat,dependencia,ambiente,personal, bienImag, proveedor, provMaq, maestro, incidenciaDsi, bienHadware, bienSoftware, bienDetalleMonitor, nutricion, personalVpnAct, personalCertificado, valGlobalSub

# Ubicacion usuario
class casAdmin(admin.ModelAdmin):
    list_display = ('codCas','descripCas','tipoCas')
    search_fields = ('tipoCas',)

# Seguridad
class usuarioAdmin(admin.ModelAdmin):
    list_display = ('num_doc','nombre','cas','usuario','clave','perfil')
    search_fields = ('usuario',)

# Register your models here.
class maestroAdmin(admin.ModelAdmin):
    list_display = ('codMaestro','descripMaestro','detalleMaestro')
    search_fields = ('codMaestro',)

class pacienteAdmin(admin.ModelAdmin):
    list_display = ('tipo_doc','num_doc','ape_pat','ape_mat','nombres','fecha_nac','cas','estado')

class examenAdmin(admin.ModelAdmin):
    list_display = ('paciente','tipo_exam','archivo_exam','estado_lectura','estado','fecha_reg','user_reg','fecha_mod','user_mod','fecha_eli','user_eli')
    search_fields = ('paciente__nombres', 'paciente__ape_pat', 'paciente__ape_mat',)

class archivoAdmin(admin.ModelAdmin):
    list_display = ('paciente','numHisCli','numBalda','estado','user_reg')
    search_fields = ('numHisCli',)

class imagenInline(admin.TabularInline):
    model = bienImag

#Anemia clinicas

class presAnemiaAdmin(admin.ModelAdmin):
    list_display = ('paciente','fechaPres','nomNefro','medPres','dosisPres','medHiePres','dosisHiePres','viaAdmPres','viaAdmHiePres','usuario')
    search_fields = ('nomNefro',)

class admiAnemiaAdmin(admin.ModelAdmin):
    list_display = ('presAnemia','fechaAdmi','nomEnfer','medAdmi','dosisAdmi','medHieAdmi','dosisHieAdmi','viaAdm','viaAdmHierro','usuario')
    search_fields = ('nomEnfer',)

class exclusionAnemiaAdmin(admin.ModelAdmin):
    list_display = ('paciente','fechaExclu','razonExclu','ObservaExclu','usuario')
    search_fields = ('razonExclu',)

class movimientoAnemiaAdmin(admin.ModelAdmin):
    list_display = ('paciente','fechaMotivo','razonMotivo','obserMotivo')
    search_fields = ('razonMotivo',)

class nutricionAdmin(admin.ModelAdmin):
    list_display = ('paciente','turno','frecuencia','fechaIngreso','fechaEvaluacion','peso','talla','imc','porcentajeCMB','porcentajeEPT','albSerica','ValGlobalSub','ingestaCalorica','ingestaProteica','diagNutricional','interveNutricional','usuario','fechaReg','pacNuevo')
    search_fields = ('frecuencia',)

#Datos de Hospitales VGS

class valGlobalSubAdmin(admin.ModelAdmin):
    list_display = ('paciente','fechaEval','ganPerPeso','camPesoCorp','duraDieta','resultDieta','tipoDieta','sintoGastro','disfuncion','cambioCapFun','grasaSubcu','atrofiaMusc','EdemaTobi','edemaSacro','ascitis','resultadoVGS','fechaReg','userReg')
    search_fields = ('resultadoVGS',)

#Datos de inventario

class bienpatAdmin(admin.ModelAdmin):
    list_display = ('codEti','propBien','desBien','serBien','modBien','marBien','situBien','valBien','estBien')
    search_fields = ('codEti',)
    inlines = [imagenInline]
    list_filter = ('propBien','desBien','serBien','modBien','marBien','situBien')

class dependenciaAdmin(admin.ModelAdmin):
    list_display = ('codDep','descDep')
    search_fields = ('codDep',)

class ambienteAdmin(admin.ModelAdmin):
    list_display = ('codAmb','descAmb','dependencia')
    search_fields = ('codAmb',)

class personalAdmin(admin.ModelAdmin):
    list_display = ('dniPer','apePatPer','apeMatPer','nomPer','sexo','fecNacPer','codPlaPer','regPer','cargoPer','nivelPer','telefoPer','correoPer','direcPer','estPer','dependencia')
    search_fields = ('dniPer',)
    ordering = ['apePatPer',]

class bienPersonalAdmin(admin.ModelAdmin):
    list_display = ('personal','bienpat')
    autocomplete_fields = ('personal','bienpat')
    search_fields = ('bienpat__codEti','personal__dniPer','personal__apePatPer')

class bienAmbienteAdmin(admin.ModelAdmin):
    list_display = ('ambiente','bienpat','personal')
    autocomplete_fields = ('ambiente','bienpat')

class bienHadwareAdmin(admin.ModelAdmin):
    list_display = ('bienpat','procesador','numeroIp','numeroMac','memoriaRam','capAlmacenamiento','uso','condicion')
    autocomplete_fields = ('bienpat',)

class bienSoftwareAdmin(admin.ModelAdmin):
    list_display = ('bienpat','sistemaOperativo','ofimatica','antivirus')
    autocomplete_fields = ('bienpat',)

class bienDetalleMonitorAdmin(admin.ModelAdmin):
    list_display = ('bienpat','pulgadas')
    autocomplete_fields = ('bienpat',)

class proveedorAdmin(admin.ModelAdmin):
    list_display = ('rucProveedor','nombreProveedor','telefProveedor','direcProveedor','estadoProveedor')
    search_fields = ('rucProveedor',)

class provMaqAdmin(admin.ModelAdmin):
    list_display = ('usobien','bienpat')
    search_fields = ('usobien',)

class incidenciaDsiAdmin(admin.ModelAdmin):
    list_display = ('personal','problema','clasiSolu','solucion','userReg','fecha_reg','numTicket','estado')
    search_fields = ('estado__codMaestro',)
    list_filter = ('estado','clasiSolu')

class personalVpnActAdmin(admin.ModelAdmin):
    list_display = ('personal','ip','usuario','clave','personalAutoriza','fechaHabilita','fechaInstalacion','observacion','fecha_reg','dato')
    autocomplete_fields = ('personal',)
    search_fields = ('usuario',)

class personalCertificadoAdmin(admin.ModelAdmin):
    list_display = ('personal','fechaSolicita','tipoCertificado','fechaInstalacion','perosnalInstala','observacion','fecha_reg')
    autocomplete_fields = ('personal',)
    search_fields = ('tipoCertificado',)

admin.site.register(cas, casAdmin)

admin.site.register(usuario, usuarioAdmin)

admin.site.register(maestro, maestroAdmin)

admin.site.register(paciente, pacienteAdmin)
admin.site.register(examen, examenAdmin)
admin.site.register(archivo, archivoAdmin)

admin.site.register(presAnemia, presAnemiaAdmin)
admin.site.register(admiAnemia, admiAnemiaAdmin)
admin.site.register(exclusionAnemia, exclusionAnemiaAdmin)
admin.site.register(movimientoAnemia, movimientoAnemiaAdmin)
admin.site.register(nutricion, nutricionAdmin)
admin.site.register(valGlobalSub, valGlobalSubAdmin)

admin.site.register(personal, personalAdmin)
admin.site.register(bienpat, bienpatAdmin)
admin.site.register(dependencia, dependenciaAdmin)
admin.site.register(ambiente, ambienteAdmin)
admin.site.register(bienPersonal, bienPersonalAdmin)
admin.site.register(bienAmbiente, bienAmbienteAdmin)
admin.site.register(bienHadware, bienHadwareAdmin)
admin.site.register(bienSoftware, bienSoftwareAdmin)
admin.site.register(bienDetalleMonitor, bienDetalleMonitorAdmin)

admin.site.register(proveedor, proveedorAdmin)
admin.site.register(provMaq, provMaqAdmin)


admin.site.register(incidenciaDsi, incidenciaDsiAdmin)
admin.site.register(personalVpnAct, personalVpnActAdmin)
admin.site.register(personalCertificado, personalCertificadoAdmin)
