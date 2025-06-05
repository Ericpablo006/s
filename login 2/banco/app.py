import mysql.connector
import hashlib

# ⚙️ Configurações do MySQL
db_config = {
    "host": "localhost",
    "user": "seu_usuario",
    "password": "sua_senha",
    "database": "sistema_login"
}

# 🔧 Criar a tabela no MySQL
def criar_tabela():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INT AUTO_INCREMENT PRIMARY KEY,
            email VARCHAR(255) UNIQUE NOT NULL,
            senha VARCHAR(255) NOT NULL
        );
    """)
    conn.commit()
    conn.close()

# 🔐 Criptografar senha
def criptografar_senha(senha):
    return hashlib.sha256(senha.encode()).hexdigest()

# 📝 Cadastrar novo usuário
def cadastrar_usuario(email, senha):
    senha_criptografada = criptografar_senha(senha)
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO usuarios (email, senha) VALUES (%s, %s)", (email, senha_criptografada))
        conn.commit()
        print("✅ Cadastro realizado com sucesso!")
    except mysql.connector.errors.IntegrityError:
        print("⚠️ E-mail já cadastrado.")
    finally:
        conn.close()

# 🔓 Fazer login
def fazer_login(email, senha):
    senha_criptografada = criptografar_senha(senha)
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE email = %s AND senha = %s", (email, senha_criptografada))
    usuario = cursor.fetchone()
    conn.close()
    if usuario:
        print("✅ Login realizado com sucesso!")
        return True
    else:
        print("❌ E-mail ou senha incorretos.")
        return False

# 🎮 Interface simples de terminal
if __name__ == "__main__":
    criar_tabela()

    while True:
        print("\n1 - Cadastrar\n2 - Login\n3 - Sair")
        opcao = input("Escolha: ")
        if opcao == '1':
            email = input("Digite seu e-mail: ")
            senha = input("Digite sua senha: ")
            cadastrar_usuario(email, senha)
        elif opcao == '2':
            email = input("E-mail: ")
            senha = input("Senha: ")
            fazer_login(email, senha)
        elif opcao == '3':
            break
        else:
            print("Opção inválida.")
