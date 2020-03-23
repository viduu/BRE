from tkinter import*
import math,random,os
from tkinter import messagebox
class BILL_CALCULATOR:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1800x1080+0+0")
        self.root.title("BILL CALCULATOR")
        bg_color="dark cyan"
        title=Label(self.root,text="BILL CALCULATOR",bd=12,relief=GROOVE,bg=bg_color,fg="white",font=("times new roman ",30,"bold"),pady=2).pack(fill=X)

        ###############################################VARIABLES#####################################################
        self.soap=IntVar()
        self.cream=IntVar()
        self.hairgel=IntVar()
        self.comb=IntVar()
        self.hairdryer=IntVar()
        self.shampoo=IntVar()
        self.maza=IntVar()
        self.frooty=IntVar()
        self.soda=IntVar()
        self.fruitjuice=IntVar()
        self.coke=IntVar()
        self.thumbsup=IntVar()
        self.rice=IntVar()
        self.pulses=IntVar()
        self.flour=IntVar()
        self.sugar=IntVar()
        self.tea=IntVar()
        self.foodoil=IntVar()
        self.pen=IntVar()
        self.pencil=IntVar()
        self.notebook=IntVar()
        self.eraser=IntVar()
        self.sharpner=IntVar()
        self.box=IntVar()
        self.cosmetic_price=StringVar()
        self.grocery_price=StringVar()
        self.softdrink_price=StringVar()
        self.stationary_price=StringVar()
        self.cosmetic_tax=StringVar()
        self.grocery_tax=StringVar()
        self.softdrink_tax=StringVar()
        self.stationary_tax=StringVar()
        self.name=StringVar()
        self.phnno=StringVar()
        
        self.billno=StringVar()
        x=random.randint(1000,9999)
        self.billno.set((x))
        self.searchbar=StringVar()
    
        
#=======================customer details==================================
        F1=LabelFrame(self.root,bd=10,relief=GROOVE,text="Customer Details",font=("Algerian",15,"bold"),fg="gold",bg=bg_color)
        F1.place(x=0,y=80,relwidth=1)

        cname_lbl=Label(F1,text="Customer Name",bg=bg_color,fg="white",font=("Algerian",18,"bold")).grid(row=0,column=0,padx=10,pady=10)
        cname_txt=Entry(F1,width=20,font="arial 15",textvariable=self.name,bd=7,relief=SUNKEN).grid(row=0,column=1,pady=10,padx=10)

        cphone_lbl=Label(F1,text="Phone Number",bg=bg_color,fg="white",font=("Algerian",18,"bold")).grid(row=0,column=2,padx=10,pady=10)
        cphone_txt=Entry(F1,width=20,font="arial 15",textvariable=self.phnno,bd=7,relief=SUNKEN).grid(row=0,column=3,pady=10,padx=10)

        c_bill_lbl=Label(F1,text="Bill Number",bg=bg_color,fg="white",font=("Algerian",18,"bold")).grid(row=0,column=4,padx=10,pady=10)
        c_bill_txt=Entry(F1,width=20,font="arial 15",textvariable=self.searchbar,bd=7,relief=SUNKEN).grid(row=0,column=5,pady=10,padx=10)
        bill_btn=Button(F1,text="SEARCH",command=self.find_bill,width=10,bd=7,font="arial 12 bold").grid(row=0,column=6,pady=10,padx=10)



        F2=LabelFrame(self.root,bd=10,relief=GROOVE,text="COSMETICS",font=("Algerian",15,"bold"),fg="gold",bg=bg_color)
        F2.place(x=5,y=180,width=330,height=380)

        ####################################COSMETICS=============================================================================

        BATH_lbl=Label(F2,text="SOAP",bg=bg_color,fg="white",font=("Algerian",18,"bold")).grid(row=0,column=0,padx=10,pady=10,sticky="w")
        bath_txt=Entry(F2,width=10,font="arial 15",textvariable=self.soap,bd=5,relief=SUNKEN).grid(row=0,column=1,pady=10,padx=10)

        cream=Label(F2,text="CREAM",bg=bg_color,fg="white",font=("Algerian",18,"bold")).grid(row=1,column=0,padx=10,pady=10,sticky="w")
        cream_txt=Entry(F2,width=10,font="arial 15",textvariable=self.cream,bd=5,relief=SUNKEN).grid(row=1,column=1,pady=10,padx=10)

        COMB=Label(F2,text="COMB",bg=bg_color,fg="white",font=("Algerian",18,"bold")).grid(row=2,column=0,padx=10,pady=10,sticky="w")
        COMB_txt=Entry(F2,width=10,font="arial 15",textvariable=self.comb,bd=5,relief=SUNKEN).grid(row=2,column=1,pady=10,padx=10)

        HAIRDRYER=Label(F2,text="HAIR DRYER",bg=bg_color,fg="white",font=("Algerian",18,"bold")).grid(row=3,column=0,padx=10,pady=10,sticky="w")
        cream_txt=Entry(F2,width=10,font="arial 15",textvariable=self.hairdryer,bd=5,relief=SUNKEN).grid(row=3,column=1,pady=10,padx=10)

        shampoo=Label(F2,text="SHAMPOO",bg=bg_color,fg="white",font=("Algerian",18,"bold")).grid(row=4,column=0,padx=10,pady=10,sticky="w")
        SHAMP_txt=Entry(F2,width=10,font="arial 15",textvariable=self.shampoo,bd=5,relief=SUNKEN).grid(row=4,column=1,pady=10,padx=10)

        HAIRGEL=Label(F2,text="HAIR GEL",bg=bg_color,fg="white",font=("Algerian",18,"bold")).grid(row=5,column=0,padx=10,pady=10,sticky="w")
        HG_txt=Entry(F2,width=10,font="arial 15",textvariable=self.hairgel,bd=5,relief=SUNKEN).grid(row=5,column=1,pady=10,padx=10)

#######################################################GROCERY##################################################################################################################################
        F3=LabelFrame(self.root,bd=10,relief=GROOVE,text="GROCERY",font=("Algerian",15,"bold"),fg="gold",bg=bg_color)
        F3.place(x=330,y=180,width=330,height=380)

        

        G1_lbl=Label(F3,text="RICE",bg=bg_color,fg="white",font=("Algerian",18,"bold")).grid(row=0,column=0,padx=10,pady=10,sticky="w")
        G1_txt=Entry(F3,width=10,font="arial 15",textvariable=self.rice,bd=5,relief=SUNKEN).grid(row=0,column=1,pady=10,padx=10)

        G2=Label(F3,text="PULSES",bg=bg_color,fg="white",font=("Algerian",18,"bold")).grid(row=1,column=0,padx=10,pady=10,sticky="w")
        G2_txt=Entry(F3,width=10,font="arial 15",textvariable=self.pulses,bd=5,relief=SUNKEN).grid(row=1,column=1,pady=10,padx=10)

        G3=Label(F3,text="FOOD OIL",bg=bg_color,fg="white",font=("Algerian",18,"bold")).grid(row=2,column=0,padx=10,pady=10,sticky="w")
        G3_txt=Entry(F3,width=10,font="arial 15",textvariable=self.foodoil,bd=5,relief=SUNKEN).grid(row=2,column=1,pady=10,padx=10)

        G4=Label(F3,text="FLOUR",bg=bg_color,fg="white",font=("Algerian",18,"bold")).grid(row=3,column=0,padx=10,pady=10,sticky="w")
        G4_txt=Entry(F3,width=10,font="arial 15",textvariable=self.flour,bd=5,relief=SUNKEN).grid(row=3,column=1,pady=10,padx=10)

        G5=Label(F3,text="SUGAR",bg=bg_color,fg="white",font=("Algerian",18,"bold")).grid(row=4,column=0,padx=10,pady=10,sticky="w")
        G5_txt=Entry(F3,width=10,font="arial 15",textvariable=self.sugar,bd=5,relief=SUNKEN).grid(row=4,column=1,pady=10,padx=10)

        G6=Label(F3,text="TEA",bg=bg_color,fg="white",font=("Algerian",18,"bold")).grid(row=5,column=0,padx=10,pady=10,sticky="w")
        G6_txt=Entry(F3,width=10,font="arial 15",textvariable=self.tea,bd=5,relief=SUNKEN).grid(row=5,column=1,pady=10,padx=10)


       
    #############################################SOFT DRINKS###################################################################################
        F4=LabelFrame(self.root,bd=10,relief=GROOVE,text="SOFT DRINKS",font=("Algerian",15,"bold"),fg="gold",bg=bg_color)
        F4.place(x=630,y=180,width=330,height=380)

        

        S1_lbl=Label(F4,text="FROOTY",bg=bg_color,fg="white",font=("Algerian",18,"bold")).grid(row=0,column=0,padx=10,pady=10,sticky="w")
        S1_txt=Entry(F4,width=10,font="arial 15",textvariable=self.frooty,bd=5,relief=SUNKEN).grid(row=0,column=1,pady=10,padx=10)

        S2=Label(F4,text="COKE",bg=bg_color,fg="white",font=("Algerian",18,"bold")).grid(row=1,column=0,padx=10,pady=10,sticky="w")
        S2_txt=Entry(F4,width=10,font="arial 15",textvariable=self.coke,bd=5,relief=SUNKEN).grid(row=1,column=1,pady=10,padx=10)

        S3=Label(F4,text="MAZA",bg=bg_color,fg="white",font=("Algerian",18,"bold")).grid(row=2,column=0,padx=10,pady=10,sticky="w")
        S3_txt=Entry(F4,width=10,font="arial 15",textvariable=self.maza,bd=5,relief=SUNKEN).grid(row=2,column=1,pady=10,padx=10)

        S4=Label(F4,text="THUMBS UP",bg=bg_color,fg="white",font=("Algerian",18,"bold")).grid(row=3,column=0,padx=10,pady=10,sticky="w")
        S4_txt=Entry(F4,width=10,font="arial 15",textvariable=self.thumbsup,bd=5,relief=SUNKEN).grid(row=3,column=1,pady=10,padx=10)

        S5=Label(F4,text="SODA",bg=bg_color,fg="white",font=("Algerian",18,"bold")).grid(row=4,column=0,padx=10,pady=10,sticky="w")
        S5_txt=Entry(F4,width=10,font="arial 15",textvariable=self.soda,bd=5,relief=SUNKEN).grid(row=4,column=1,pady=10,padx=10)

        S6=Label(F4,text="FRUIT JUICE",bg=bg_color,fg="white",font=("Algerian",18,"bold")).grid(row=5,column=0,padx=10,pady=10,sticky="w")
        S6_txt=Entry(F4,width=10,font="arial 15",textvariable=self.fruitjuice,bd=5,relief=SUNKEN).grid(row=5,column=1,pady=10,padx=10)

#######################################################STATIONARY######################################################################33
        F5=LabelFrame(self.root,bd=10,relief=GROOVE,text="STATIONARY",font=("Algerian",15,"bold"),fg="gold",bg=bg_color)
        F5.place(x=950,y=180,width=330,height=380)

        S1_lbl=Label(F5,text="PEN",bg=bg_color,fg="white",font=("Algerian",18,"bold")).grid(row=0,column=0,padx=10,pady=10,sticky="w")
        S1_txt=Entry(F5,width=10,font="arial 15",textvariable=self.pen,bd=5,relief=SUNKEN).grid(row=0,column=1,pady=10,padx=10)

        S2=Label(F5,text="PENCIL",bg=bg_color,fg="white",font=("Algerian",18,"bold")).grid(row=1,column=0,padx=10,pady=10,sticky="w")
        S2_txt=Entry(F5,width=10,font="arial 15",textvariable=self.pencil,bd=5,relief=SUNKEN).grid(row=1,column=1,pady=10,padx=10)

        S3=Label(F5,text="SHARPNER",bg=bg_color,fg="white",font=("Algerian",18,"bold")).grid(row=2,column=0,padx=10,pady=10,sticky="w")
        S3_txt=Entry(F5,width=10,font="arial 15",textvariable=self.sharpner,bd=5,relief=SUNKEN).grid(row=2,column=1,pady=10,padx=10)

        S4=Label(F5,text="NOTEBOOK",bg=bg_color,fg="white",font=("Algerian",18,"bold")).grid(row=3,column=0,padx=10,pady=10,sticky="w")
        S4_txt=Entry(F5,width=10,font="arial 15",textvariable=self.notebook,bd=5,relief=SUNKEN).grid(row=3,column=1,pady=10,padx=10)

        S5=Label(F5,text="ERASER",bg=bg_color,fg="white",font=("Algerian",18,"bold")).grid(row=4,column=0,padx=10,pady=10,sticky="w")
        S5_txt=Entry(F5,width=10,font="arial 15",textvariable=self.eraser,bd=5,relief=SUNKEN).grid(row=4,column=1,pady=10,padx=10)

        S6=Label(F5,text="BOX",bg=bg_color,fg="white",font=("Algerian",18,"bold")).grid(row=5,column=0,padx=10,pady=10,sticky="w")
        S6_txt=Entry(F5,width=10,font="arial 15",textvariable=self.box,bd=5,relief=SUNKEN).grid(row=5,column=1,pady=10,padx=10)

#####################################################BILL CALCULATOR##########################################################################
        F6=Frame(self.root,bd=10,relief=GROOVE)
        F6.place(x=1280,y=180,width=250,height=380)
        BILL_TITLE=Label(F6,text="BILL CALCULATOR",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        SCROLL_Y=Scrollbar(F6,orient=VERTICAL)
        self.textarea=Text(F6,yscrollcommand=SCROLL_Y.set)
        SCROLL_Y.pack(side=RIGHT,fill=Y)
        SCROLL_Y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)

        ################################button frame####################################################################################################3
        F7=LabelFrame(self.root,bd=10,relief=GROOVE,text="BILL MENU",font="Algerian 15 bold",fg="gold",bg=bg_color)
        F7.place(x=0,y=560,relwidth=1,height=240)

        m1_lbl=Label(F7,text="TOTAL COSMETIC PRICE",bg=bg_color,fg="white",font=("Algerian",15,"bold")).grid(row=0,column=0,padx=20,pady=1,sticky="w")
        m1_txt=Entry(F7,width=18,font="arial 15",textvariable=self.cosmetic_price,bd=7,relief=SUNKEN).grid(row=0,column=1,pady=1,padx=20)

        m2=Label(F7,text="TOTAL GROCERY PRICE",bg=bg_color,fg="white",font=("Algerian",15,"bold")).grid(row=1,column=0,padx=20,pady=1,sticky="w")
        m2_txt=Entry(F7,width=18,font="arial 15",textvariable=self.grocery_price,bd=7,relief=SUNKEN).grid(row=1,column=1,pady=1,padx=20)

        m3=Label(F7,text="TOTAL SOFT DRINK PRICE",bg=bg_color,fg="white",font=("Algerian",15,"bold")).grid(row=2,column=0,padx=20,pady=1,sticky="w")
        m3_txt=Entry(F7,width=18,font="arial 15",textvariable=self.softdrink_price,bd=7,relief=SUNKEN).grid(row=2,column=1,pady=1,padx=20)

        M4=Label(F7,text="TOTAL STATIONARY PRICE",bg=bg_color,fg="white",font=("Algerian",15,"bold")).grid(row=3,column=0,padx=20,pady=1,sticky="w")
        M4_txt=Entry(F7,width=18,font="arial 15",textvariable=self.stationary_price,bd=7,relief=SUNKEN).grid(row=3,column=1,pady=1,padx=20)

        M5=Label(F7,text="COSMETIC TAX",bg=bg_color,fg="white",font=("Algerian",15,"bold")).grid(row=0,column=2,padx=20,pady=1,sticky="w")
        M5_txt=Entry(F7,width=18,font="arial 15",textvariable=self.cosmetic_tax,bd=7,relief=SUNKEN).grid(row=0,column=3,pady=1,padx=20)

        M6=Label(F7,text="GROCERY TAX",bg=bg_color,fg="white",font=("Algerian",15,"bold")).grid(row=1,column=2,padx=20,pady=1,sticky="w")
        M6_txt=Entry(F7,width=18,font="arial 15",textvariable=self.grocery_tax,bd=7,relief=SUNKEN).grid(row=1,column=3,pady=1,padx=20)

        M7=Label(F7,text="STATIONARY TAX",bg=bg_color,fg="white",font=("Algerian",15,"bold")).grid(row=3,column=2,padx=20,pady=1,sticky="w")
        M7_txt=Entry(F7,width=18,font="arial 15",textvariable=self.stationary_tax,bd=7,relief=SUNKEN).grid(row=3,column=3,pady=1,padx=20)

        M8=Label(F7,text="SOFTDRINK TAX",bg=bg_color,fg="white",font=("Algerian",15,"bold")).grid(row=2,column=2,padx=20,pady=1,sticky="w")
        M8_txt=Entry(F7,width=18,font="arial 15",textvariable=self.softdrink_tax,bd=7,relief=SUNKEN).grid(row=2,column=3,pady=1,padx=20)

        Btn_f=Frame(F7,bd=7,relief=GROOVE)
        Btn_f.place(x=1030,width=479,height=165)


        total_btn=Button(Btn_f,command=self.total,text="TOTAL",bg="cadetblue",fg="black",pady=12,bd=5,width=9,font="arial 12 bold").grid(row=0,column=0,padx=5,pady=5)
        GB_btn=Button(Btn_f,command=self.bill_cal,text="BILL",bg="cadetblue",fg="black",pady=12,bd=5,width=9,font="arial 12 bold").grid(row=0,column=1,padx=5,pady=5)
        CLEAR_btn=Button(Btn_f,command=self.cleardata,text="CLEAR",bg="cadetblue",fg="black",pady=12,bd=5,width=9,font="arial 12 bold").grid(row=0,column=2,padx=5,pady=5)
        EXIT_btn=Button(Btn_f,command=self.exit,text="EXIT",bg="cadetblue",fg="black",pady=12,bd=5,width=9,font="arial 12 bold").grid(row=0,column=3,padx=5,pady=5)
        P_btn=Button(Btn_f,text="PAYMENT",bg="cadetblue",fg="black",pady=12,bd=5,width=9,font="arial 12 bold").grid(row=1,padx=5,pady=5)
        self.WEL_BILL()
    def total(self):
        self.c_sp=self.soap.get()*40
        self.cr=self.cream.get()*140
        self.hg=self.hairgel.get()*240
        self.sh=self.shampoo.get()*160
        self.co=self.comb.get()*20
        self.hd=self.hairdryer.get()*280
        self.tcp=float(
               self.c_sp+
               self.cr+
               self.hg+
               self.sh+
               self.co+
               self.hd
            )
        self.cosmetic_price.set("Rs."+str(self.tcp))
        self.c_tax=round((self.tcp*0.05),2)
        self.cosmetic_tax.set("Rs."+str(self.c_tax))
        self.r=self.rice.get()*140
        self.p=self.pulses.get()*220
        self.fo=self.foodoil.get()*240
        self.fl=self.flour.get()*190
        self.sg=self.sugar.get()*70
        self.t=self.tea.get()*45
        self.tgp=float(
               self.r+
               self.p+
               self.fo+
               self.fl+
               self.sg+
               self.t
            )
        self.grocery_price.set("Rs."+str(self.tgp))
        self.g_tax=round((self.tgp*0.05),2)
        self.grocery_tax.set("Rs."+str(self.g_tax))
        self.fr=self.frooty.get()*40
        self.m=self.maza.get()*40
        self.ck=self.coke.get()*40
        self.tu=self.thumbsup.get()*40
        self.sd=self.soda.get()*20
        self.fj=self.fruitjuice.get()*80
        self.scp=float(
               self.fr+
               self.m+
               self.ck+
               self.tu+
               self.sd+
               self.fj
            )
        self.softdrink_price.set("Rs."+str(self.scp))
        self.sd_tax=round((self.scp*0.02),2)
        self.softdrink_tax.set("Rs."+str(self.sd_tax))
        self.pn=self.pen.get()*10
        self.pl=self.pencil.get()*5
        self.e=self.eraser.get()*5
        self.sp=self.sharpner.get()*5
        self.b=self.box.get()*40
        self.n=self.notebook.get()*80
        self.stcp=float(
               self.pn+
               self.pl+
               self.e+
               self.sp+
               self.b+
               self.n
            )
        self.stationary_price.set("Rs."+str(self.stcp))
        self.s_tax=round((self.stcp*0.05),2)
        self.stationary_tax.set("Rs."+str(self.s_tax))

        self.TOTAL=float(self.tcp+
                         self.tgp+
                         self.scp+
                         self.stcp+
                         self.c_tax+
                         self.g_tax+
                         self.sd_tax+
                         self.s_tax)
    def WEL_BILL(self):
         self.textarea.delete('1.0',END)
         self.textarea.insert(END,"=====THE TWINKLE STORE====")
         self.textarea.insert(END,f"\n\nBill Number :{self.billno.get()}")
         self.textarea.insert(END,f"\nName : {self.name.get()}")
         self.textarea.insert(END,f"\nPhone number :{self.phnno.get()}")
         self.textarea.insert(END,f"\n==========================")
         self.textarea.insert(END,f"\n Products\t  QTY    \tPrice")
         self.textarea.insert(END,f"\n==========================")
         
         
    def bill_cal(self):
        if self.name.get()=="" or self.phnno.get()=="":
            messagebox.showerror("ERROR!!","Customer details are must")
        elif self.cosmetic_price.get()=="Rs.0.0" and self.grocery_price.get()=="Rs.0.0" and self.stationary_price.get()=="Rs.0.0" and self.softdrink_price.get()=="Rs.0.0":
            messagebox.showerror("ERROR!!","YOU HAVEN'T PURCHASED ANYTHING ")
            
        else:
            self.WEL_BILL()
#===========================================cosmetics===============
            if self.soap.get()!=0:
                self.textarea.insert(END,f"\n  SOAP\t     {self.soap.get()}\t    {self.c_sp}")
            if self.cream.get()!=0:
                self.textarea.insert(END,f"\n  CREAM\t     {self.cream.get()}\t    {self.cr}")
            if self.hairgel.get()!=0:
                self.textarea.insert(END,f"\n  HAIRGEL\t   {self.hairgel.get()}     \t{self.hg}")
            if self.hairdryer.get()!=0:
                self.textarea.insert(END,f"\n  HAIRDRYER\t {self.hairdryer.get()}     \t{self.hd}")
            if self.comb.get()!=0:
                self.textarea.insert(END,f"\n  COMB\t     {self.comb.get()}     \t{self.co}")
            if self.shampoo.get()!=0:
                self.textarea.insert(END,f"\n  SHAMPOO\t   {self.shampoo.get()}\t    {self.sh}")    
#================================softdrinks=============================================        
            if self.frooty.get()!=0:
                self.textarea.insert(END,f"\n  FROOTY\t    {self.frooty.get()}     \t{self.fr}")
            if self.coke.get()!=0:
                self.textarea.insert(END,f"\n  COKE\t     {self.coke.get()}     \t{self.ck}")
            if self.maza.get()!=0:
                self.textarea.insert(END,f"\n  MAZA\t     {self.maza.get()}     \t{self.m}")
            if self.soda.get()!=0:
                self.textarea.insert(END,f"\n  SODA\t     {self.soda.get()}     \t{self.sd}")
            if self.thumbsup.get()!=0:
                self.textarea.insert(END,f"\n  THUMBSUP\t  {self.thumbsup.get()}     \t{self.tu}")
            if self.fruitjuice.get()!=0:
                self.textarea.insert(END,f"\n  FRUITJUICE\t{self.fruitjuice.get()}     \t{self.fj}")     

#================================stationary=============================================        
            if self.pen.get()!=0:
                self.textarea.insert(END,f"\n  PEN\t     {self.pen.get()}     \t{self.pn}")
            if self.pencil.get()!=0:
                self.textarea.insert(END,f"\n  PENCIL\t    {self.pencil.get()}     \t{self.pl}")
            if self.eraser.get()!=0:
                self.textarea.insert(END,f"\n  ERASER\t    {self.eraser.get()}     \t{self.e}")
            if self.notebook.get()!=0:
                self.textarea.insert(END,f"\n  NOTEBOOK\t  {self.notebook.get()}     \t{self.n}")
            if self.box.get()!=0:
                self.textarea.insert(END,f"\n  BOX\t     {self.box.get()}     \t{self.b}")
            if self.sharpner.get()!=0:
                self.textarea.insert(END,f"\n  SHARPNER\t  {self.sharpner.get()}     \t{self.sp}")     

#================================GROCERy=============================================        
            if self.rice.get()!=0:
                self.textarea.insert(END,f"\n  RICE\t     {self.rice.get()}     \t{self.r}")
            if self.pulses.get()!=0:
                self.textarea.insert(END,f"\n  PULSES\t    {self.pulses.get()}     \t{self.p}")
            if self.foodoil.get()!=0:
                self.textarea.insert(END,f"\n  FOODOIL\t   {self.foodoil.get()}     \t{self.fo}")
            if self.sugar.get()!=0:
                self.textarea.insert(END,f"\n  SUGAR\t     {self.sugar.get()}     \t{self.sg}")
            if self.tea.get()!=0:
                self.textarea.insert(END,f"\n  TEA\t     {self.tea.get()}     \t{self.t}")
            if self.flour.get()!=0:
                self.textarea.insert(END,f"\n  FLOUR\t     {self.flour.get()}     \t{self.fl}")     


            self.textarea.insert(END,f"\n--------------------------")
            if self.cosmetic_tax.get()!="Rs.0.0":
                self.textarea.insert(END,f"\nCosmetic Tax\t\t  {self.cosmetic_tax.get()}")
            if self.grocery_tax.get()!="Rs.0.0":
                self.textarea.insert(END,f"\nGrocery Tax\t\t  {self.grocery_tax.get()}")
            if self.softdrink_tax.get()!="Rs.0.0":
                self.textarea.insert(END,f"\nSoftdrink Tax\t\t {self.softdrink_tax.get()}")
            if self.stationary_tax.get()!="Rs.0.0":
                self.textarea.insert(END,f"\nStationary Tax\t\t{self.stationary_tax.get()}")
            self.textarea.insert(END,f"\n--------------------------")   
            self.textarea.insert(END,f"\nTOTAL BILL :\t\tRs.{str(self.TOTAL)}")
            self.textarea.insert(END,f"\n--------------------------")
            self.save_bill()
    def save_bill(self):
         op=messagebox.askyesno("Save Bill","Do you want to save the BILL?")
         if op>0:
             self.bill_data=self.textarea.get('1.0',END)
             fi=open("BILLCALCULATOR/BILLS/"+str(self.billno.get())+".txt","w")
             fi.write(self.bill_data)
             fi.close()
             messagebox.showinfo("SAVED!!",f"Bill:{self.billno.get()} Successfully SAVED!!!")
         else:
             return 

    def find_bill(self):
        present="no"
        for i in os.listdir("BILLCALCULATOR/BILLS/"):
            if i.split('.')[0]==self.searchbar.get():
                fi=open(f"BILLCALCULATOR/BILLS/{i}","r")
                self.textarea.delete('1.0',END)
                for d in fi:
                    self.textarea.insert(END,d)
                fi.close()
                present="yes"
        if present=="no":                     
             messagebox.showerror("ERROR!!","Invalid bill no.")
        
    def cleardata(self):
         op=messagebox.askyesno("CLEAR","Do you really want to CLEAR ?")
         if op>0:
             self.soap.set(0)
             self.cream.set(0)
             self.hairgel.set(0)
             self.comb.set(0)
             self.hairdryer.set(0)
             self.shampoo.set(0)
             self.maza.set(0)
             self.frooty.set(0)
             self.soda.set(0)
             self.fruitjuice.set(0)
             self.coke.set(0)
             self.thumbsup.set(0)
             self.rice.set(0)
             self.pulses.set(0)
             self.flour.set(0)
             self.sugar.set(0)
             self.tea.set(0)
             self.foodoil.set(0)
             self.pen.set(0)
             self.pencil.set(0)
             self.notebook.set(0)
             self.eraser.set(0)
             self.sharpner.set(0)
             self.box.set(0)
             self.cosmetic_price.set("")
             self.grocery_price.set("")
             self.softdrink_price.set("")
             self.stationary_price.set("")
             self.cosmetic_tax.set("")
             self.grocery_tax.set("")
             self.softdrink_tax.set("")
             self.stationary_tax.set("")
             self.name.set("")
             self.phnno.set("")
        
             self.billno.set("")
             x=random.randint(1000,9999)
             self.billno.set(str(x))
             self.searchbar.set('')
             self.WEL_BILL()
    
    def exit(self):
        op=messagebox.askyesno("EXIT","Do you really want to exit?")
        if op>0:
            self.root.destroy()
            


        

root=Tk()
obj=BILL_CALCULATOR(root)
root.mainloop()
