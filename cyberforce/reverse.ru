require 'openssl'
require 'base64'

$pass = 'CatsAtTheMansion'

def encrypt(plain)
  cipher = OpenSSL::Cipher::AES.new(128, :ECB).encrypt

  cipher.key = $pass

  encrypted = cipher.update(plain) + cipher.final
  return encrypted
end

def decrypt(ciphertext)
  cipher = OpenSSL::Cipher::AES.new(128, :ECB).decrypt

  cipher.key = $pass
  decrypted = cipher.update(ciphertext) + cipher.final
end

def main()
  puts "enter string"
  input = gets.chomp
 
  enc = encrypt(input)

  dec = decrypt(enc)
  puts decrypt(Base64.decode64("ekiJZkuVbZFmpqarq3vvVw=="))
  puts enc
  puts dec
end

main()