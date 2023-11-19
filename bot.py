class fbcal:
    def get_nama(self, jumlah_halaman):
        nama_indonesia = ['Budi', 'Siti', 'Ahmad', 'Dewi', 'Hadi', 'Ani', 'Joko', 'Rini', 'Eko', 'Lina',
                        'Hendra', 'Siska', 'Rizki', 'Dina', 'Yudi', 'Nina', 'Irfan', 'Maya', 'Adi', 'Rina',
                        'Taufik', 'Wati', 'Farhan', 'Lia', 'Agus', 'Diana', 'Rudi', 'Fitri', 'Firman', 'Ayu',
                        'Joko', 'Sari', 'Andi', 'Ratna', 'Eko', 'Citra', 'Bambang', 'Lina', 'Fajar', 'Yuni',
                        'Bambang', 'Lia', 'Hendri', 'Rita', 'Wahyu', 'Dian', 'Bella', 'Jaka', 'Yanti', 'Yoga',
                        'Tri', 'Mira', 'Doni', 'Eka', 'Putri', 'Rahmat', 'Siska', 'Haryanto', 'Aisyah', 'Ridwan',
                        'Rina', 'Firman', 'Yanti', 'Rizal', 'Santi', 'Gandi', 'Rima', 'Yoga', 'Hesti', 'Surya',
                        'Arin', 'Yoga', 'Sari', 'Firman', 'Kartika', 'Ade', 'Yulia', 'Irfan', 'Dina', 'Bayu',
                        'Desi', 'Firman', 'Anita', 'Yoga', 'Ratna', 'Rifki', 'Lina', 'Dedi', 'Ika', 'Yoga',
                        'Tri', 'Dian', 'Ricky', 'Rini', 'Hadi', 'Nina', 'Wawan', 'Sari', 'Saputra', 'Dina',
                        'Yusuf', 'Lia', 'Herman', 'Kartika', 'Indra', 'Yuni', 'Dedi', 'Wati', 'Yoga', 'Rina']

        nama_vietnam = ['Minh', 'Linh', 'Trung', 'Hoa', 'Quoc', 'Mai', 'Tuan', 'Thi', 'Dat', 'Hien',
                        'Khanh', 'Nga', 'Quan', 'My', 'Viet', 'Phuong', 'Nam', 'Lan', 'Cuong', 'Thao',
                        'Duc', 'Ha', 'Tu', 'Diep', 'Nhan', 'An', 'Thu', 'Huy', 'Trang', 'Hoang',
                        'Nhung', 'Dung', 'Phuc', 'Lien', 'Phat', 'Hang', 'Hieu', 'Tram', 'Nhat', 'Tuyen',
                        'Phuong', 'Nam', 'Hai', 'Lan', 'Thanh', 'Tam', 'Hung', 'Ngoc', 'Loan', 'Khoa',
                        'Tien', 'Thanh', 'Thu', 'Cuong', 'Quynh', 'Son', 'Thuy', 'Phong', 'My', 'Quyen',
                        'Phuc', 'Nga', 'Hao', 'Bao', 'Trinh', 'Tuan', 'Anh', 'Lien', 'Hai', 'Hang',
                        'Duong', 'Huong', 'Tinh', 'Kien', 'Mai', 'Duc', 'Lien', 'Binh', 'Ngoc', 'Tam',
                        'Hai', 'Thi', 'Hoang', 'Loan', 'Tan', 'Quyen', 'Tien', 'Phuc', 'Quynh', 'Hung',
                        'Hien', 'Tuyen', 'Dat', 'Nhat', 'Ha', 'Quan', 'Thu', 'Trang', 'Hung', 'Yen']

        nama_china = ['Wei', 'Li', 'Zhang', 'Liu', 'Chen', 'Yang', 'Huang', 'Zhao', 'Wu', 'Zhou',
                    'Xu', 'Sun', 'Ma', 'Zhu', 'Hu', 'Guo', 'Luo', 'Wang', 'Lin', 'Gao',
                    'He', 'Xie', 'Deng', 'Yuan', 'Han', 'Tang', 'Feng', 'Song', 'Pan', 'Yao',
                    'Qian', 'Shi', 'Rong', 'Xia', 'Jin', 'Hua', 'Jing', 'Wei', 'Xiao', 'Yi',
                    'Jiang', 'Cao', 'Yu', 'Mao', 'Chang', 'Hou', 'Dai', 'Wang', 'Cheng', 'Xiong',
                    'Li', 'Duan', 'Zeng', 'Cui', 'Bao', 'Yin', 'Qiu', 'Yuan', 'Zeng', 'Wang',
                    'Gu', 'Zheng', 'Fang', 'Shen', 'Yang', 'Zou', 'Pan', 'Zhu', 'Liang', 'Fang',
                    'Yu', 'Wu', 'Guo', 'Yin', 'Feng', 'Chang', 'Song', 'Chen', 'Lu', 'Zhang',
                    'Yi', 'Tang', 'Jin', 'Zhou', 'Wang', 'Li', 'Xu', 'Yuan', 'Wu', 'Zhu',
                    'Cheng', 'Liu', 'Hu', 'Zheng', 'Huang', 'Guo', 'Chang', 'Yuan', 'Wang', 'Chen']

        nama_thailand = ['Sawasdee', 'Araya', 'Chai', 'Dara', 'Ittipol', 'Kanya', 'Lek', 'Manop', 'Nuan', 'Orapan',
                        'Preecha', 'Rungrawee', 'Somsak', 'Thao', 'Udon', 'Varee', 'Wijit', 'Xaiyaboun', 'Yai', 'Zee',
                        'Phichai', 'Siriporn', 'Tawan', 'Chaiyo', 'Thidarat', 'Prasert', 'Pimchan', 'Noppadol', 'Narong',
                        'Kritsana', 'Nuttapong', 'Supaporn', 'Wipawee', 'Sakda', 'Chutima', 'Apinya', 'Surin', 'Napaporn', 'Arnon',
                        'Siri', 'Witoon', 'Sarin', 'Thongchai', 'Arnon', 'Sakul', 'Parichat', 'Somsak', 'Chavalit', 'Supaporn',
                        'Wijitra', 'Thanapon', 'Arun', 'Anong', 'Vichai', 'Wichai', 'Patcharin', 'Sarawut', 'Saranya', 'Charnchai',
                        'Kulthida', 'Pisit', 'Aree', 'Sombat', 'Samrit', 'Suchada', 'Prateep', 'Pojanee', 'Narong', 'Arunee',
                        'Aroon', 'Boonmee', 'Chuan', 'Duang', 'Jitlada', 'Kittisak', 'Montri', 'Pachara', 'Preeda', 'Somjit',
                        'Sukanya', 'Supat', 'Sutas', 'Thamrong', 'Thongbai', 'Waraporn', 'Wimol', 'Yongyuth', 'Thitima', 'Chalerm']

        nama_india = ['Aarav', 'Aanya', 'Advait', 'Aisha', 'Arya', 'Dev', 'Diya', 'Ishaan', 'Kabir', 'Kiara',
                    'Krish', 'Mia', 'Neha', 'Rahul', 'Riya', 'Rohan', 'Sanvi', 'Shanaya', 'Shiv', 'Sofia',
                    'Aaradhya', 'Aryan', 'Anaya', 'Aryan', 'Anaya', 'Aadya', 'Arjun', 'Ishika', 'Ishan', 'Ishita',
                    'Kavya', 'Laksh', 'Mira', 'Om', 'Pari', 'Rishabh', 'Saisha', 'Tanvi', 'Tara', 'Veer',
                    'Virat', 'Yuvan', 'Zara', 'Zayn', 'Anika', 'Vihaan', 'Aditi', 'Arnav', 'Anvi', 'Aadi',
                    'Dhruv', 'Divya', 'Evaan', 'Ishana', 'Ishwar', 'Jiya', 'Kiaan', 'Krisha', 'Lavya', 'Mahi',
                    'Misha', 'Niyati', 'Nivaan', 'Parth', 'Prisha', 'Rudra', 'Sara', 'Samaira', 'Vanya', 'Yash',
                    'Advika', 'Arya', 'Aanya', 'Aarush', 'Aahana', 'Aanya', 'Arjun', 'Aadya', 'Aanya', 'Aarav',
                    'Advait', 'Aadya', 'Aarna', 'Anvi', 'Arjun', 'Advait', 'Anika', 'Anaya', 'Aanya', 'Advika']

        nama_amerika = ['Emma', 'Liam', 'Olivia', 'Noah', 'Ava', 'Isabella', 'Sophia', 'Jackson', 'Lucas', 'Aiden',
                        'Elijah', 'Harper', 'Mia', 'Evelyn', 'Camila', 'Abigail', 'Luna', 'Carter', 'Riley', 'Chloe',
                        'James', 'Oliver', 'Amelia', 'Benjamin', 'Ethan', 'Isaac', 'Alexander', 'Sebastian', 'Aria', 'Gabriel',
                        'Scarlett', 'Madison', 'Grayson', 'Zoe', 'Mila', 'Layla', 'Henry', 'Lily', 'Lillian', 'Mason', 'Logan',
                        'Hannah', 'Nathan', 'Ella', 'Levi', 'Sadie', 'Caleb', 'Matthew', 'Samuel', 'Avery', 'Wyatt',
                        'Hunter', 'Andrew', 'Jack', 'Charlotte', 'David', 'Aubrey', 'Sofia', 'Ellie', 'Amaya', 'Grace',
                        'Addison', 'Victoria', 'Elena', 'Lucy', 'Madelyn', 'Mackenzie', 'Adrian', 'Alexa', 'Brooklyn', 'Natalie',
                        'Zoey', 'Samantha', 'Penelope', 'Mila', 'Claire', 'Aaliyah', 'Gabriella', 'Nicholas', 'Sarah', 'Anna',
                        'Hazel', 'Taylor', 'Eva', 'Ariana', 'Nora', 'Harrison', 'Eli', 'Bella', 'Skylar', 'Julian', 'Lila']

        nama_gamer = ['ShadowHunter', 'EpicSniper', 'DragonSlayer', 'CyberPirate', 'MysticWarrior', 'NinjaAssassin', 'SteelPhoenix',
                    'LunarReaper', 'VortexBlade', 'QuantumGambit', 'StarDustRider', 'ChronoWanderer', 'TechMage', 'VoidSorcerer',
                    'SpectralJester', 'PandoraRogue', 'NeonSpecter', 'ZephyrStriker', 'RogueRevenant', 'SilentSpecter', 'MegaByteWarrior',
                    'AstroGladiator', 'ViperVanguard', 'RapidFireX', 'InfinitySorcerer', 'ThunderSerpent', 'SilverHavoc', 'ApexPredator',
                    'GalacticRonin', 'NebulaNomad', 'CyberProwler', 'QuantumBlitz', 'LaserShadow', 'StarForgeMage', 'VenomWarden',
                    'JinxedJoker', 'CrypticRaider', 'BlazeBlizzard', 'PulseRaider', 'VenomSorcerer', 'StormySamurai', 'CrimsonReaper',
                    'PhantomWarden', 'TwilightValkyrie', 'ChronoHunter', 'LethalLynx', 'ThunderFury', 'ArcanePhoenix', 'EclipseSorcerer',
                    'SpectralReaper', 'VortexValkyrie', 'WarpWizard', 'MysticBlaze', 'OmegaOutlaw', 'ViperValkyrie', 'QuantumReaper',
                    'NovaSorcerer', 'InfernoSpecter', 'ZenithZephyr', 'OmegaOracle', 'FrostFireMage', 'VenomVortex', 'EternalRonin',
                    'CyberNinja', 'SpartanShadow', 'GalacticGambit', 'TwilightSpecter', 'StarChaser', 'DoomRider', 'QuantumQuasar',
                    'ViperVindicator', 'NovaNomad', 'ChronoCorsair', 'EpicEnigma', 'WarpWanderer', 'LunarLynx', 'VortexVanguard',
                    'FrostyPhantom', 'NeonNebula', 'CrimsonCipher', 'QuantumQuiver', 'EclipseEnchantress', 'MegaByteMystic', 'BlazeBard',
                    'SpectralSorcerer', 'VortexVirtuoso', 'RogueRanger', 'EpicExorcist', 'InfinityInferno', 'ThunderTempest', 'NebulaNinja',
                    'CyberCorsair', 'AstroArcher', 'QuantumQuill', 'ViperVigilante', 'OmegaOracle', 'EtherealEnigma', 'ShadowStalker']

        nama_perusahaan = ['TechVista', 'WebSphere', 'DataPulse', 'CloudConnect', 'NetNexa', 'CyberCrafter', 'InfoSprint',
                            'WebWarp', 'ByteBoost', 'QuantumNet', 'DigitalLink', 'InfinitiSphere', 'StreamlineNet', 'TechnoTrek',
                            'GlobalMesh', 'Connectify', 'VortexWave', 'SwiftStream', 'NexaLink', 'TechNectar', 'DigitalDynamo',
                            'WebWavelength', 'ByteBlast', 'QuantumQuotient', 'InfraPulse', 'EpicEdge', 'DigitalDomain', 'WebVista',
                            'SwiftSync', 'TechBurst', 'NetNectar', 'DataDart', 'QuantumQuest', 'WebWeave', 'VividVelocity', 'ByteBurst',
                            'TechTide', 'InfraPulse', 'WebWave', 'ConnectCraze', 'QuantumQuasar', 'DigitalDart', 'ByteBeam', 'WebWhiz',
                            'NetNexa', 'TechnoTrail', 'QuantumQuest', 'WebWander', 'DataDynamo', 'EpicEdge', 'ConnectCraft', 'TechTrek',
                            'VortexView', 'SwiftSync', 'InfoSphere', 'QuantumQuotient', 'WebWhirl', 'ByteBlaze', 'TechTide', 'DataDash',
                            'QuantumQuasar', 'ConnectCraft', 'VividVelocity', 'WebWarp', 'DigitalDynamo', 'ByteBoost', 'InfoSprint',
                            'NetNectar', 'SwiftStream', 'QuantumNet', 'TechNectar', 'WebWeave', 'DigitalDomain', 'Connectify', 'DataPulse',
                            'VortexWave', 'CloudConnect', 'StreamlineNet', 'WebWavelength', 'ByteBlast', 'EpicEdge', 'QuantumQuotient',
                            'InfraPulse', 'SwiftSync', 'VortexView', 'DataDash', 'ConnectCraft', 'WebWave', 'TechTide', 'QuantumQuest',
                            'ByteBurst', 'DigitalDart', 'InfoSphere', 'NetNectar', 'WebWhirl', 'ByteBlaze', 'ConnectCraze', 'VividVelocity']

        nama_inggris = ['James', 'Emma', 'Oliver', 'Ava', 'William', 'Sophia', 'Benjamin', 'Isabella', 'Elijah', 'Charlotte',
                        'Lucas', 'Amelia', 'Mason', 'Mia', 'Logan', 'Harper', 'Jackson', 'Evelyn', 'Aiden', 'Abigail',
                        'Ethan', 'Emily', 'Sebastian', 'Elizabeth', 'Carter', 'Avery', 'Wyatt', 'Sofia', 'Henry', 'Grace',
                        'Owen', 'Chloe', 'Grayson', 'Lily', 'Liam', 'Scarlett', 'Ezra', 'Aria', 'Levi', 'Ella',
                        'Caleb', 'Madison', 'Hunter', 'Layla', 'Jack', 'Nora', 'Luke', 'Camila', 'Daniel', 'Penelope',
                        'Olivia', 'Michael', 'Riley', 'Nicholas', 'Zoey', 'Gabriel', 'Hannah', 'Matthew', 'Aubrey', 'David',
                        'Ellie', 'Joseph', 'Lillian', 'John', 'Addison', 'Samuel', 'Brooklyn', 'Ryan', 'Stella', 'Isaac',
                        'Victoria', 'Julian', 'Natalie', 'Evan', 'Willow', 'Nathan', 'Lucy', 'Aaron', 'Kylie', 'Isaiah',
                        'Anna', 'Adam', 'Zoe', 'Jason', 'Layla', 'Nolan', 'Mila', 'Christian', 'Leah', 'Alex', 'Audrey',
                        'Jonathan', 'Aaliyah', 'Connor', 'Allison', 'Thomas', 'Savannah', 'Leo', 'Aurora', 'Jeremiah', 'Nevaeh']

        nama_arab = ['Mohammed', 'Aisha', 'Omar', 'Fatima', 'Ahmed', 'Zainab', 'Ali', 'Nour', 'Layla', 'Youssef',
                    'Zayd', 'Amina', 'Khaled', 'Sana', 'Mustafa', 'Mariam', 'Omar', 'Leila', 'Hassan', 'Jana',
                    'Yusuf', 'Hala', 'Abdullah', 'Aya', 'Amir', 'Lina', 'Tariq', 'Layla', 'Ibrahim', 'Farida',
                    'Zakaria', 'Noor', 'Hamza', 'Sarah', 'Khalid', 'Nada', 'Rami', 'Samira', 'Bilal', 'Soraya',
                    'Nasser', 'Yara', 'Jamal', 'Salma', 'Faisal', 'Amina', 'Sami', 'Amani', 'Mahmoud', 'Zara',
                    'Yousef', 'Maya', 'Adnan', 'Amal', 'Fadi', 'Safia', 'Riad', 'Selma', 'Najib', 'Samiya',
                    'Mounir', 'Huda', 'Nidal', 'Mona', 'Jamil', 'Rasha', 'Amer', 'Lama', 'Tamer', 'Hanan',
                    'Bassam', 'Layla', 'Rafiq', 'Dina', 'Tarek', 'Samar', 'Ismail', 'Fayruz', 'Jafar', 'Farida',
                    'Nabeel', 'Shadia', 'Iyad', 'Rania', 'Malik', 'Maha', 'Saad', 'Sawsan', 'Rashid', 'Habiba',
                    'Ziad', 'Afaf', 'Yasin', 'Siham', 'Maher', 'Lubna', 'Nidal', 'Amina', 'Waleed', 'Sara']

        nama_jepang = ['Haruto', 'Yua', 'Sota', 'Himari', 'Riku', 'Koharu', 'Ren', 'Hina', 'Yuito', 'Akari',
                    'Ryota', 'Nana', 'Sora', 'Yui', 'Taiga', 'Kanna', 'Kaito', 'Sakura', 'Haruki', 'Mio',
                    'Daichi', 'Rina', 'Kota', 'Yuna', 'Kazuki', 'Mana', 'Shota', 'Aoi', 'Minato', 'Yume',
                    'Hiroto', 'Kaho', 'Yuto', 'Hikari', 'Kakeru', 'Miku', 'Takumi', 'Hana', 'Tatsuki', 'Hinata',
                    'Ryusei', 'Aika', 'Kenta', 'Kaede', 'Yuma', 'Konomi', 'Renya', 'Yuka', 'Sho', 'Kotone',
                    'Tsubasa', 'Yuzuki', 'Kazuya', 'Saki', 'Hayato', 'Riko', 'Toya', 'Riko', 'Yuuki', 'Nagisa',
                    'Takeru', 'Miyu', 'Reo', 'Yukino', 'Keita', 'Kotomi', 'Koki', 'Rin', 'Hiroko', 'Kento',
                    'Airi', 'Seiya', 'Ayaka', 'Ryoma', 'Yuri', 'Tatsuya', 'Mizuki', 'Yudai', 'Ayane', 'Kosuke',
                    'Risa', 'Kohei', 'Aya', 'Sosuke', 'Miyuki', 'Kazuma', 'Akane', 'Tomoya', 'Erika', 'Ryuto']

        nama_rusia = ['Ivan', 'Ekaterina', 'Dmitri', 'Anastasia', 'Aleksandr', 'Natalia', 'Sergei', 'Yelena', 'Mikhail', 'Olga',
                    'Vladimir', 'Irina', 'Andrei', 'Yulia', 'Nikolai', 'Anna', 'Pavel', 'Tatiana', 'Yuri', 'Elena',
                    'Dmitry', 'Svetlana', 'Alexey', 'Maria', 'Artem', 'Ksenia', 'Igor', 'Eva', 'Roman', 'Victoria',
                    'Fedor', 'Nina', 'Konstantin', 'Marina', 'Oleg', 'Elizaveta', 'Viktor', 'Katerina', 'Ilya', 'Alina',
                    'Vasili', 'Nadia', 'Andrey', 'Ekaterina', 'Maxim', 'Larisa', 'Grigory', 'Nastya', 'Petr', 'Galina',
                    'Anton', 'Sofia', 'Semyon', 'Valentina', 'Yegor', 'Darya', 'Ruslan', 'Yana', 'Boris', 'Valeria',
                    'Leonid', 'Tanya', 'Evgeny', 'Elena', 'Vitaly', 'Polina', 'Yaroslav', 'Natalya', 'Rostislav', 'Anya',
                    'Vyacheslav', 'Irina', 'Denis', 'Inna', 'Kirill', 'Ludmila', 'Sergey', 'Margaret', 'Yakov', 'Raisa',
                    'Nikita', 'Veronika', 'Vladislav', 'Sofia', 'Maksim', 'Alexandra', 'Stepan', 'Valeriya', 'Timur', 'Anfisa']

        nama_spanyol = ['Alejandro', 'Sofía', 'Mateo', 'Valentina', 'Martín', 'Lucía', 'Leonardo', 'Emma', 'Santiago', 'Mia',
                        'Daniel', 'Isabella', 'Sebastián', 'Camila', 'Matías', 'Victoria', 'Felipe', 'Olivia', 'Nicolás', 'Emilia',
                        'Benjamín', 'Ava', 'Lucas', 'Sofía', 'Emiliano', 'Aria', 'Diego', 'Elena', 'Samuel', 'Valeria',
                        'Alexander', 'Juana', 'Joaquín', 'Martina', 'Gabriel', 'Isabel', 'Tomás', 'Antonella', 'Adrián', 'Luciana',
                        'Ángel', 'Julia', 'David', 'Renata', 'Samuel', 'Manuela', 'Miguel', 'Josefina', 'Víctor', 'Diana',
                        'Juan', 'Paula', 'José', 'Ximena', 'Rafael', 'Fernanda', 'Javier', 'Mariana', 'Cristian', 'Camila',
                        'Carlos', 'Ana', 'Andrés', 'Valerie', 'Esteban', 'Daniela', 'Fernando', 'Raquel', 'Francisco', 'Laura',
                        'Luis', 'Natalia', 'Rodrigo', 'Catalina', 'Gustavo', 'Alejandra', 'Ignacio', 'Bianca', 'Jorge', 'Rosa',
                        'Mario', 'Sara', 'Pedro', 'Clara', 'Roberto', 'Liliana', 'Héctor', 'Eva', 'Julio', 'Luna']

        jumlah_total_nama = jumlah_halaman
        semua_nama = nama_indonesia + nama_vietnam + nama_china + nama_thailand + nama_india + nama_amerika + nama_gamer + nama_perusahaan + nama_inggris + nama_arab + nama_jepang + nama_rusia + nama_spanyol
        random.shuffle(semua_nama)

        nama_final = []
        for i in range(0, jumlah_total_nama, 2):
            nama_pasangan = f"{semua_nama[i]} {semua_nama[i + 1]}"
            if nama_pasangan not in nama_final:
                nama_final.append(nama_pasangan)

        ganyang = []
        for i, nama in enumerate(nama_final):
            ganyang.append(nama)

        while len(ganyang) < jumlah_total_nama:
            random.shuffle(semua_nama)
            for i in range(0, jumlah_total_nama - len(ganyang), 2):
                nama_pasangan = f"{semua_nama[i]} {semua_nama[i + 1]}"
                if nama_pasangan not in ganyang:
                    ganyang.append(nama_pasangan)
        self.nama_random = ganyang
    def ceklogin(self):
        self.logo = "\n\n⠀⠀⠀⢀⡤⢤⢄⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⣼⡅⠠⢀⡈⢀⣙⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⠤⠤⢤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⢸⠀⠀⠀⠈⠙⠿⣝⢇⠀⠀⣀⣠⠤⠤⠤⠤⣤⡤⠚⠁⠀⠀⠀⠀⠀⠉⠢⡀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⢧⡀⠀⠀⠠⣄⠈⢺⣺⡍⠀⠀⠀⠀⣠⠖⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡄⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠸⡆⢀⠘⣔⠄⠑⠂⠈⠀⡔⠤⠴⠚⡁⠀⠀⢀⠀⠀⠀⣠⠔⢶⡢⡀⠀⠠⡇⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⢠⣇⠀⢃⡀⠁⠀⠀⠀⡸⠃⢀⡴⠊⢀⠀⠀⠈⢂⡤⠚⠁⠀⠀⠙⢿⠀⠉⡇⠀⠀⠀⠀⠀\n⠀⠀⠀⣠⠾⣹⢤⢼⡆⠀⠀⠀⠀⠀⠀⠈⢀⠞⠁⠀⢠⣴⠏⠀⠀⠀⠀⠀⠀⠸⡇⠀⢇⠀⠀⠀⠀\n⠀⠀⣾⢡⣤⡈⠣⡀⠙⠒⠀⠀⠀⠀⣀⠤⠤⣤⠤⣌⠁⢛⡄⠀⠀⠀⠀⠀⠠⡀⢇⠀⠘⣆⠀⢀⡄⡄             Aungthor : DemonLords27☠\n⠀⠀⣿⢻⣿⣿⣄⡸⠀⡆⠀⠒⣈⣩⣉⣉⡈⠉⠉⠢⣉⠉⠀⠀⠀⠀⠀⠀⠀⢣⠈⠢⣀⠈⠉⢁⡴⠃\n⠀⢀⢿⣿⣿⡿⠛⠁⠀⢻⣿⣿⣿⣿⣿⣿⣿⣷⣦⣄⣸⢿⠀⠀⠀⠀⠀⠀⠀⠸⡄⠀⡇⠉⠉⠁⠀⠀             Version  : 0.1\n⣠⣞⠘⢛⡛⢻⣷⣤⡀⠈⡎⣿⣿⣿⣿⣿⣿⣿⣿⣿⠹⠏⠀⠀⠀⠀⠀⠀⠀⠀⠇⢰⡇⠀⠀⠀⠀⠀\n⠻⣌⠯⡁⢠⣸⣿⣿⣷⡄⠁⠈⢻⢿⣿⣿⣿⣿⠿⠋⠃⠰⣀⠀⠀⠀⠀⠀⠀⠀⠀⣾⠇⠀⠀⠀⠀⠀\n⠀⠀⠉⢻⠨⠟⠹⢿⣿⢣⠀⠀⢨⡧⣌⠉⠁⣀⠴⠊⠑⠀⡸⠛⠀⠀⠀⠀⠀⣸⢲⡟⠀⠀⠀⠀⠀⠀\n⠀⠀⣠⠏⠀⠀⠀⠉⠉⠁⠀⠐⠁⠀⠀⢉⣉⠁⠀⠀⢀⠔⢷⣄⠀⠀⠀⠀⢠⣻⡞⠀⠀⠀⠀⠀⠀⠀\n⠀⢠⠟⡦⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⢾⠉⠀⣹⣦⠤⣿⣿⡟⠁⠀⠀⠀⢀⣶⠟⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠈⠙⣦⣁⡎⢈⠏⢱⠚⢲⠔⢲⠲⡖⠖⣦⣿⡟⠀⣿⡿⠁⣠⢔⡤⠷⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⢿⣟⠿⡿⠿⠶⢾⠶⠾⠶⠾⠞⢻⠋⠏⣸⠁⠀⡽⠓⠚⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⢸⡏⠳⠷⠴⠣⠜⠢⠜⠓⠛⠊⠀⢀⡴⠣⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⣏⠒⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠊⠁⢀⣀⣀⠴⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠘⢦⡀⠀⠀⠀⠀⠀⠀⢀⣀⠴⠖⠒⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠉⠑⠒⠒⠐⠒⠛⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"
        try:
            open(".cuki.txt").read()
            self.menu()
        except FileNotFoundError:
            self.sihsih()
            pr("[bold green]"+self.logo)
            cok = input("Masukkan Cookies   : ")
            with open(".cuki.txt", 'w') as f: f.write(cok)
            self.ceklogin()
    def proxy(self):
        self.proksi= []
        proki = requests.get("https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all").text
        for prox in proki.splitlines():
            self.proksi.append(prox)
    def genpayload(self):
         self.data = {
            'av': re.search('"actorID":"(.*?)"',                                    self.po).group(1), 
            '__user': re.search('"actorID":"(.*?)"',                                self.po).group(1),
            '__a': re.search("__a=(.*?)&",                                          self.po).group(1),
            '__hs': re.search('"haste_session":"(.*?)"',                            self.po).group(1), 
            '__ccg': 'EXCELLENT', 
            '__rev': re.search('{"rev":(.*?)}',                                     self.po).group(1),
            '__hsi': re.search('"hsi":"(.*?)"',                                     self.po).group(1),
            '__comet_req': re.search('__comet_req=(.*?)&',                          self.po).group(1), 
            'fb_dtsg': re.search('"DTSGInitialData",\[\],\{"token":"(.*?)"',        self.po).group(1), 
            'jazoest': re.search('jazoest=(.*?),',                                  self.po).group(1),
            'lsd': re.search('"LSD",\[\],\{"token":"(.*?)"',                        self.po).group(1), 
            '__aaid': '0', 
            '__spin_r': re.search('"__spin_r":(.*?),',                              self.po).group(1), 
            '__spin_b': re.search('"__spin_b":(.*?),',                              self.po).group(1), 
            '__spin_t': re.search('"__spin_t":(.*?),',                              self.po).group(1), 
            'fb_api_caller_class': 'RelayModern', 
            'fb_api_req_friendly_name': self.frename, 
            'variables': json.dumps(self.var), 
            'server_timestamps': 'true',
            'doc_id': self.docpg
         }
    def lodcuki(self):
        try:
            self.cok = open('.cuki.txt').read()
            self.cuki = {}
            for x in self.cok.split("; "):
                a, x = x.split("=")
                self.cuki[a] = x
            self.cuki = {key: value.strip() for key, value in self.cuki.items()}
        except FileNotFoundError:
            pr("[bold red]File .cuki.txt tidak ditemukan. Silakan login.")
            self.ceklogin()
        except Exception as e:
            pr("[bold red]Error membaca kuki:", str(e))
            os.remove('.cuki.txt')
            self.ceklogin()
    def login(self):
        self.ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
        self.hader = {
            'Accept':'*/*',
            'Accept-Encoding':'gzip, deflate, br',
            'Accept-Language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,es;q=0.6',
            'Content-Length':'1625',
            'Content-Type':'application/x-www-form-urlencoded',
            'Sec-Ch-Prefers-Color-Scheme': 'light',
            'Sec-Ch-Ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
            'Sec-Ch-Ua-Full-Version-List': '"Google Chrome";v="119.0.6045.124", "Chromium";v="119.0.6045.124", "Not?A_Brand";v="24.0.0.0"',
            'Sec-Ch-Ua-Mobile': '?0',
            'Sec-Ch-Ua-Model': '',
            'Sec-Ch-Ua-Platform': 'Windows',
            'Sec-Ch-Ua-Platform-Version': '10.0.0',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent':self.ua
        }
        self.lodcuki()
        self.graph = "https://web.facebook.com/api/graphql/"
        url = "https://www.facebook.com/pages/"
        self.po = demon.get(url, cookies=self.cuki).text
        self.nama = re.search('"NAME":"(.*?)"',self.po).group(1)
        self.idu = re.search('"USER_ID":"(.*?)"',self.po).group(1)
        if self.idu == '0':
            pr(f"[bold red]{self.logo}\n\nCookies Expired ")
            time.sleep(5)
            os.remove('.cuki.txt')
            sys.exit()
    def sihsih (self):
        try:
            os.system('clear')
        except os.error:
            try:
                os.system('cls')
            except os.error:
                # Handle the case where neither 'cls' nor 'clear' is available
                print("Clearing the screen is not supported on this system.")
    def cretpage(self):
        self.frename = "AdditionalProfilePlusCreationMutation"
        self.docpg = "5296879960418435"
        self.hader.update({
            'Origin': 'https://www.facebook.com',
            'Referer': 'https://www.facebook.com/pages/?category=your_pages&ref=bookmarks',
            'X-Fb-Friendly-Name': self.frename,
            'X-Fb-Lsd': re.search('"LSD",\[\],\{"token":"(.*?)"',self.po).group(1)
        })
        self.genpayload()
        self.grappost = demon.post(self.graph, headers=self.hader, cookies=self.cuki, data=self.data, proxies={'http': self.random_proxy()})
        with open('rest.txt', 'w') as f:
            f.write(json.dumps(self.genpayload()))
        self.check_page(self.grappost.text)
    def random_proxy(self):
        return random.choice(self.proksi)
    def check_page(self, response_data):
        if 'for (;;);' in response_data:
            response_data = response_data[len('for (;;);'):]
        response_json = json.loads(response_data)
        if "data" in response_json and "additional_profile_plus_create" in response_json["data"]:
            additional_profile = response_json["data"]["additional_profile_plus_create"]["additional_profile"]
            page = response_json["data"]["additional_profile_plus_create"]["page"]
            name_error = response_json["data"]["additional_profile_plus_create"]["name_error"]
            error_message = response_json["data"]["additional_profile_plus_create"]["error_message"]
            if name_error is not None:
                pr(pn(name_error,title="Pages-ERROR", width=50, style='bold red'))
            elif error_message is not None:
                pr(pn(f"[bold White]Nama    : [bold green]{self.nama_halaman}",title="Pages-FAILED", width=50, style='bold red'))
            elif additional_profile and "id" in additional_profile and page and "id" in page:
                pr(pn(f"[bold White]Nama    : [bold green]{self.nama_halaman} \n[bold white]ID Page : [bold cyan]{additional_profile['id']}",title="Pages-OK", width=50, style='bold green'))
                self.okpg+=1
            else:
                print("Gagal")
            self.ksabar(int(self.durasi)*60)
    def ksabar(self,duration):
        progress = 0
        total_iterations = int(duration / 0.1)
        while progress <= 100:
            sys.stdout.write("\r{:.0f}%  ".format(progress) + "■" * int(progress / 2) + "□" * (50 - int(progress / 2)) + "  {:.0f}%".format(progress))
            sys.stdout.flush()
            time.sleep(0.1)
            progress += 100 / total_iterations
        sys.stdout.write("\n")
        sys.stdout.flush()
    def polow(self):
        pr(pn(f"[bold white]Gunakan Semua Page  y/n ?",title=f"Follow", width=40, style='bold green'))
        pilih = input("Masukkan Pilihan : ")
        if pilih in ['y','Y']:
            self.listakun()
            for name, idp in self.pages.items():
                self.var = {"profile_id":idp}
                self.frename = "CometProfileSwitchMutation"
                self.docpg = "7240611932633722"
                self.genpayload()
                loginkan = demon.post(self.graph, headers=self.hader, cookies=self.cuki, data=self.data).cookies.get_dict()
                self.frename = "CometUserFollowMutation"
                self.docpg="6792650737481329"
                cek = name, idp
                self.var = {"input":{"attribution_id_v2":"ProfileCometTimelineListViewRoot.react,comet.profile.timeline.list,via_cold_start,1700073346208,530046,190055527696468,","is_tracking_encrypted":'false',"subscribe_location":"PROFILE","subscribee_id":"100053626245325","tracking":'null',"actor_id":idp,"client_mutation_id":"1"},"scale":1.5}
                self.genpayload()
                b = self.cuki['c_user']
                if b == idp:
                    del self.cuki['i_user']
                else:
                    self.cuki.update(loginkan)
                
                time.sleep(20)
                post = demon.post(self.graph, headers=self.hader, data=self.data, cookies=self.cuki).text
                try:
                    cek = re.search('"subscribe_status":"(.*?)"', post).group(1)
                    pr(pn(f"Status   : Berhasil \nNama     : {name}\nID       : {idp}",title='OK', width=40, style='bold green'))
                except Exception:
                    pr(pn(f"Status   : Gagal \nNama     : {name}\nID       : {idp}",title='FAILED', width=40, style='bold red'))
        elif pilih in ['n', 'N']:
            self.frename = "CometUserFollowMutation"
            self.docpg="6792650737481329"
            self.var = {"input":{"attribution_id_v2":"ProfileCometTimelineListViewRoot.react,comet.profile.timeline.list,via_cold_start,1700073346208,530046,190055527696468,","is_tracking_encrypted":'false',"subscribe_location":"PROFILE","subscribee_id":"100053626245325","tracking":'null',"actor_id":self.idu,"client_mutation_id":"1"},"scale":1.5}
            self.genpayload()
            post = demon.post(self.graph, headers=self.hader, data=self.data, cookies=self.cuki).text
            try:
                cek = re.search('"subscribe_status":"(.*?)"', post).group(1)
                pr(pn(f"Status   : Berhasil \nNama     : {self.nama}\nID       : {self.idu}",title='OK', width=40, style='bold green'))
            except Exception:
                pr(pn(f"Status   : Gagal \nNama     : {self.nama}\nID       : {self.idu}",title='FAILED', width=40, style='bold red'))
    def listakun(self):
        self.frename = "FeedComposerCometRootQuery"
        self.docpg = "6723185644465112"
        self.var = {"hasStory":'false',"isFooterButtonModularizationEnabled":'false',"privacySelectorRenderLocation":"COMET_COMPOSER","profileID":re.search('"actorID":"(.*?)"',self.po).group(1),"scale":1.5,"storyID":""}
        self.genpayload()
        post = demon.post(self.graph, headers=self.hader, cookies=self.cuki, data=self.data).text
        nama = re.findall('"name":"(.*?)"', post)
        idp = re.findall('"id":"(.*?)"', post)
        self.pages = {}
        for name, id_pengguna in zip(nama, idp):
            if name.lower() not in ["friends", "everyone"]:
                self.pages[name] = id_pengguna
        if "i_user" in self.cuki:
            self.pages['Original Account'] = self.cuki['c_user']
    def buat_halaman_input(self):
        pr(pn("[white][[red]1[white]][bold white]  Buat Halaman Dengan Nama Random   \n[white][[red]2[white]][bold white]  Buat Halaman Dengan Nama Manual\n[white][[red]*[white]][bold white]  Default/Skip(Random Nama)",title="Pages-Creation", width=78, style='bold green'))
        pilihan_nama = input("[*] Masukkan Pillihan   : ").lower()
        if pilihan_nama in ['01', '1']:
            self.buat_halaman_otomatis()
        elif pilihan_nama in ['02', '2']:
            self.buat_halaman_manual()
        else:
           self.buat_halaman_otomatis()
    def buat_halaman(self, nama_halaman):
        self.login()
        self.frename = "AdditionalProfilePlusCreationMutation"
        self.docpg = "5296879960418435"
        self.var = {
                "input": {
                "bio": "Rand Sfk Bot Pages",
                "categories": ["2256"],
                "creation_source": "comet",
                "name": nama_halaman,
                "page_referrer": "launch_point",
                "actor_id": re.search('"actorID":"(.*?)"', self.po).group(1),
                "client_mutation_id": "2"
            }
        }
        self.nama_halaman = nama_halaman
        self.cretpage()
    def buat_halaman_otomatis(self):
        self.get_nama(self.total_halaman)
        self.durasi = input("Beri Delay Agar Terhindar Dari Checkpoint (Menit) : ")
        for nama in self.nama_random:
            self.buat_halaman(nama)  
    def buat_halaman_manual(self):
        for _ in range(self.total_halaman):
            nama_halaman = input("Masukkan Nama Page: ")
            self.buat_halaman(nama_halaman)
    def cengakun(self):
        totpg = 0
        self.listakun()
        lol = self.pages
        for name, id_pengguna in lol.items():
            totpg+=1
            pr(pn(f"[bold white]Nama  : [bold black]{name}\n[bold white]ID    : [bold cyan]{id_pengguna}",title=f"Your Pages {str(totpg)}", width=40, style='bold green'))
        pilihan = input("Pilih: ")
        if pilihan.isdigit() and int(pilihan) and int(pilihan) <= len(lol):
            selected_name, selected_id = list(lol.items())[int(pilihan) - 1]
            if selected_name == "Original Account":
                del self.cuki['i_user']
                newcuki = "; ".join(self.cuki)
                with open('.cuki.txt', 'w') as cuk:
                    cuk.write(newcuki)
                self.var = {"profile_id":selected_id}
            else:
                pr(pn(f"[bold white]Nama  : [bold black]{name}\n[bold white]ID    : [bold cyan]{id_pengguna}",title=f"Your Pages {str(totpg)}", width=40, style='bold green'))
                self.var = {"profile_id":selected_id}
            self.frename = "CometProfileSwitchMutation"
            self.docpg = "7240611932633722"
            self.genpayload()
            loginkan = demon.post(self.graph, headers=self.hader, cookies=self.cuki, data=self.data).cookies.get_dict()
            url = "https://www.facebook.com/pages/"
            cuki = '&'.join([f'{key}={value}' for key, value in loginkan.items()])
            hasilcuk = f'{self.cok}; {cuki}'
            with open('.cuki.txt', 'w') as cuk:
                cuk.write(hasilcuk)
        else:
            print("Pages Yang Mana KONTOL")
    def menu(self):
        self.login()
        self.sihsih()
        pr("[bold green]"+self.logo)
        pr(pn(f"[bold white]                          Nama  : [bold black]{str(self.nama)}\n[bold white]                          Id    : [bold cyan]{str(self.idu)}",title="Login-Sebagai", width=78, style='bold green'))
        if "i_user" in self.cuki:
            pr(pn("[white][[red]2[white]][bold white]  Follow Account By Pages Or Real Account\n[white][[red]3[white]][bold white]  Change Account",title="Pages-Menu", width=78, style='bold green'))
        else:
            pr(pn("[white][[red]1[white]][bold white]  Create Pages Facebook   \n[white][[red]2[white]][bold white]  Follow Account By Pages Or Real Account\n[white][[red]3[white]][bold white]  Change Account",title="Account-Menu", width=78, style='bold green'))
        pilih = input("Masukkan Pilihan  : ")
        self.proxy()
        if pilih in ['01', '1']:
            self.okpg = 0
            self.total_halaman = int(input("Masukkan jumlah halaman yang ingin dibuat: "))
            self.buat_halaman_input()
            pr("Halaman Terbuat : ",str(self.okpg))
        elif pilih in ['02', '2']:
            self.polow()
        elif pilih in ['03', '3']:
            self.cengakun()
        else:
            pr("[bold yellow]Input Yang Benar!!")
            self.menu()
if __name__ == "__main__":
    import requests,re,json,random,time,os,sys
    from bs4 import BeautifulSoup as bs
    from rich import print as pr
    from rich.console import Console
    from rich.panel import Panel as pn
    demon = requests.Session()
    medusa = requests.Session()
    gas = fbcal()
    gas.ceklogin()
