from tkinter import *
from tkinter.ttk import *
from database import *
from tkhtmlview import *



def ventanaPrincipal():

    def agregar():
        print(variable.get())
    
    def borrar():
        pass

    v = Tk()
    v.title("Khenry - Base de Conocimientos v1.01")
    v.geometry('480x540')
    v.resizable(0,0)
    n = Notebook(v)
    n.pack(fill=BOTH, expand=True)

    # Frames para notebooks

    tab1 = Frame(n)
    tab1.grid(row=0, column=0)
    tab2 = Frame(n)
    tab2.grid(row=0, column=0, sticky='ne')
    tab3 = Frame(n)
    tab3.grid(row=0, column=0)

    tab4 = Frame(n)
    tab4.grid(row=0, column=0, sticky='ne')
    tab5 = Frame(n)
    tab5.grid(row=0, column=0, sticky='ne')

    n.add(tab1, text="Portada")
    n.add(tab2, text="Útlimos Agregados")
    n.add(tab3, text="Buscar Documentos")
    n.add(tab4, text="Agregar Datos")
    n.add(tab5, text=" + ")

    # Portada

    portada = Canvas(tab1, width=474, height=216)
    portada.grid(row=0, column=0)
    img = PhotoImage(file="ksrc/A.png")
    portada.create_image(1,40, anchor=NW, image=img)
    Label(tab1, text="Khenry", font=("Georgia", 38)).grid(row=1, column=0)
    Label(tab1, text="Base de conocimientos").grid(row=2, column=0)
    Label(tab1, text=" ").grid(row=3, column=0)
    Label(tab1, text="Dedicada al Dr. Erique Cáceres Nieto", font=("Georgia", 12)).grid(row=4, column=0)
    Label(tab1, text="Herramienta desarrollada por:", font=("Georgia", 11)).grid(row=5, column=0)
    link_portada = HTMLLabel(tab1, html="<center><a href='http://helloperseo.party' style='font-size: 10px;'>helloperseo</a></center>")
    link_portada.grid(row=6, column=0)
    link_portada.config(height=2, width=9)
    Label(tab1, text="El usuario es responsable por uso que le da a esta herramienta", font=("Georgia", 10), foreground="#900C3F").grid(row=7, column=0)
    
    # LISTAR ÚLTIMOS

    Label(tab2, text=" ", width=20).grid(row=0, column=0, sticky='w', padx=10)
    Label(tab2, text="Selecciona una categoría: ", width=31).grid(row=1, column=0, sticky='w', padx=10)
    OptionList1 = ['Selecciona Categoría','Filosofía', 'Derecho', 'Matemáticas', 'Sociales', 'Física', 'Ciencia', 'Computación', 'Inteligencia Artificial', 'Ingeniería', 'Biología', 'Química', 'Lengua', 'Linguistica', 'Literatura']
    var1 = StringVar(tab2)
    var1.set(OptionList1[0])
    CATEGORIA_VIEW = OptionMenu(tab2, var1, *OptionList1)
    CATEGORIA_VIEW.grid(row=1, column=1, sticky='w', padx=10)
    CATEGORIA_VIEW.config(width=18)
    Label(tab2, text=" .", width=20).grid(row=2, column=0, sticky='w', padx=10)

    # BUSCAR ELEMENTOS

    Label(tab3, text="Buscar por título").grid(row=0, column=0, sticky="w", padx=10, pady=10)
    titulo = Entry(tab3)
    titulo.grid(row=0, column=1)
    titulo.config(width=29)
    Button(tab3, text="Buscar").grid(row=0, column=2)
    Label(tab3, text="Buscar por etiqueta").grid(row=1, column=0, sticky="w", padx=10, pady=10)
    etiqueta = Entry(tab3)
    etiqueta.grid(row=1, column=1)
    etiqueta.config(width=29)
    Button(tab3, text="Buscar").grid(row=1, column=2)
    Label(tab3, text="Buscar por autor").grid(row=2, column=0, sticky="w", padx=10, pady=10)
    autor  = Entry(tab3)
    autor.grid(row=2, column=1)
    autor.config(width=29)
    Button(tab3, text="Buscar").grid(row=2, column=2)



    # FORMULARIO DE AGREGAR DATOS TAB4

    Label(tab4, text="AGREGA NUEVO DOCUMENTO").grid(row=0, column=0, pady=10, columnspan=2)
    Label(tab4, text="Categoría", width=10).grid(row=1, column=0, sticky='w', padx=10)
    OptionList = ['Selecciona Categoría','Filosofía', 'Derecho', 'Matemáticas', 'Sociales', 'Física', 'Ciencia', 'Computación', 'Inteligencia Artificial', 'Ingeniería', 'Biología', 'Química', 'Lengua', 'Linguistica', 'Literatura']
    variable = StringVar(tab4)
    variable.set(OptionList[0])
    CATEGORIA = OptionMenu(tab4, variable, *OptionList)
    CATEGORIA.grid(row=1, column=1, sticky='w', padx=10)
    CATEGORIA.config(width=18)
    Label(tab4, text="Nombre del Libro/Documento/Artículo").grid(row=3, column=0, sticky='w', padx=10)
    NOMBRE = Entry(tab4)
    NOMBRE.grid(row=4, column=0, columnspan=3, sticky='we', padx=10)
    Label(tab4, text="Editorial").grid(row=5, column=0, sticky='w', padx=10)
    EDITORIAL = Entry(tab4)
    EDITORIAL.grid(row=6, column=0, columnspan=3, sticky='we', padx=10)
    Label(tab4, text="Año").grid(row=7, column=0, sticky='w', padx=10)
    ANIO = Entry(tab4)
    ANIO.grid(row=8, column=0, columnspan=3, sticky='we', padx=10)
    Label(tab4, text="URL").grid(row=9, column=0, sticky='w', padx=10)
    URL = Entry(tab4)
    URL.grid(row=10, column=0, columnspan=3, sticky='we', padx=10)
    # CARATULA =
    Label(tab4, text="Nombre del Autor").grid(row=11, column=0, sticky='w', padx=10)
    NOMBRE_AUTOR = Entry(tab4)
    NOMBRE_AUTOR.grid(row=12, column=0, columnspan=3, sticky='we', padx=10)
    Label(tab4, text="Apellido del Autor").grid(row=13, column=0, sticky='w', padx=10)
    APELLIDOS_AUTOR = Entry(tab4)
    APELLIDOS_AUTOR.grid(row=14, column=0, columnspan=3, sticky='we', padx=10)
    OTROS_AUTORES = Checkbutton(tab4, text="¿Otros autores?: et al.")
    OTROS_AUTORES.grid(row=15, column=0, columnspan=3, sticky='we', padx=10, pady=3)
    Label(tab4, text="Institución").grid(row=16, column=0, sticky='w', padx=10)
    INSTITUCION = Entry(tab4)
    INSTITUCION.grid(row=17, column=0, columnspan=3, sticky='we', padx=10)
    Label(tab4, text="Etiquetas separadas por comas").grid(row=18, column=0, sticky='w', padx=10)
    ETIQUETAS = Entry(tab4)
    ETIQUETAS.grid(row=19, column=0, columnspan=3, sticky='we', padx=10)
    # FECHA_REGISTRO = 
    Label(tab4, text="Notas adicionales").grid(row=20, column=0, sticky='w', padx=10)
    NOTAS = Entry(tab4)
    NOTAS.grid(row=21, column=0, columnspan=3, sticky='we', padx=10)
    Label(tab4, text="  ").grid(row=22, column=0, sticky='w', padx=10)
    Button(tab4, text="Agregar", command=agregar).grid(row=23, column=0, columnspan=2, sticky='e', padx=10)
   


        




    v.mainloop()

ventanaPrincipal()