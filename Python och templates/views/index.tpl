<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title>Nabo</title>
		<link rel="stylesheet" href="/static/style.css">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
	</head>

	<header>
		<p>nabologga.... Fungerar inte med css.</p>
	</header>

	<body>
		<div id="signin">

			<h3>Logga in</h3>	
				<form action="/home/" method="POST" class="form">
				
					<p class="email">
						<input required type="email" name="mail" id="email" placeholder="Email">			
					</p>

					<p class="password">
						<input required type="password" name="pwd" id="password" placeholder="Lösenord">	
					</p>

					<p class="submit">
						<input name="sign_in" type="submit" value="Logga in">
					</p>
				</form>
		</div>


		<div id="signUp">
			<h3>Skapa andvändare</h3>	
				<form action="/myProfile/" method="POST" class="form">
				
					<p class ="name">
						<input required type="text" name="name" id="name" placeholder="Förnamn">	
					</p>
						
					<p class="surname">
						<input required type="text" name="surname" id="surname" placeholder="Efternamn">	
					</p>
					
					<p class="adress">
						<input required type="text" name="adress" id="adress" placeholder="Adress">	
					</p>
					
					<p class="email">
						<input required type="email" name="email" id="email" placeholder="Email">			
					</p>

					<p class="password">
						<input type="password" required name="pwd_1" id="password" placeholder="Lösenord" onchange="form.pwd2.pattern = this.value;>	
					</p>

					<p class="password">
						<input type="password" required name="pwd_2" id="password" placeholder="Bekräfta lösenord">	
					</p>
					
					<p class="submit">
						<input name="register" type="submit" value="Registrera">
					</p>
				</form>
		</div>


	</body>

	<footer>
		<a href="contact.html">Kontakta oss</a>
		<a href="about.html">Om Nabo</a>
		<a href="help.html">Hjälp</a>
	</footer>
</html>


