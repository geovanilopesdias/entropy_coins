<DOCTYPE! html>
<html lang="pt-br">
	<head>
		<meta charset="UTF-8">
		<link rel="stylesheet" href="entropia-estilo.css">
		<?php
			$numero_de_moedas = $_POST["nMoedas"];
			$lancamentos_a_repetir = $_POST["nLancamentos"];
			
			function lanca_moedas($m, $l){
				$banco_de_lancamentos = array();
				for ($cl = 0; $cl < $l; $cl++){
					$lancamento = array();
					for ($cm = 0; $cm < $m; $cm++){$lancamento[] = rand(0, 1);}
					
					$banco_de_lancamentos[] = $lancamento;}
				
				return $banco_de_lancamentos;}
			
			function exibe_lancamentos($lanc_set){
				echo "<table><caption>Resultados:</caption>";
				for($i = 1; $i <= count($lanc_set); $i++){
					echo "<tr><td>".$i."º lançamento:</td>";
					foreach($lanc_set[($i-1)] as $lanc){
						if ($lanc == 1) {echo "<td><img src='cara.svg'></td>";}
						else {echo "<td><img src='coroa.svg'></td>";}
					} echo "</tr>";} echo "</table>";}
			
			function conta_resultados_iguais($lanc_set){
				$contagem_todas_caras = 0; 
				foreach($lanc_set as $lanc){
					$contagem_caras = 0;
					for ($i = 0; $i < count($lanc); $i++){$contagem_caras += $lanc[$i];}
					if($contagem_caras == count($lanc) || $contagem_caras == 0){$contagem_todas_caras++;}
				}
				return $contagem_todas_caras;}
				
			function exibe_repeticoes($repeticoes){
				switch ($repeticoes){
					case "0": echo "<h3>Em nenhum dos lançamentos as moedas caíram todas igualmente.</h3>"; break;
					case "1": echo "<h3>As moedas caíram todas igualmente uma única vez!</h3>"; break;
					default: echo "<h3>As moedas caíram todas igualmente $repeticoes vezes!</h3>";}}
		?>
	</head>
	<body>
		<header>
			<h1>Entropia de Moedas</h1>
			<h2>Por Geovani L. Dias</h2>
			<?php
				$lancamento = lanca_moedas($numero_de_moedas, $lancamentos_a_repetir);
				exibe_repeticoes(conta_resultados_iguais($lancamento));
				echo "<p>Confira, a seguir, o resultado de cada lançamento das $numero_de_moedas moedas lançadas $lancamentos_a_repetir vezes:</p>";
				exibe_lancamentos($lancamento);
			?>
		</header>
		<div>
			
		</div>
	</body>
</html>
