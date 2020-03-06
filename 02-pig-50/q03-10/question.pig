-- Pregunta
-- ===========================================================================
-- 
-- Obtenga los cinco (5) valores más pequeños de la 3ra columna.
-- Escriba el resultado a la carpeta `output` del directorio actual.
-- 
fs -rm -f -r output;
--
-- >>> Escriba su respuesta a partir de este punto <<<
--

x = LOAD 'data.tsv' USING PigStorage('\t')
    AS (f1:CHARARRAY,
	f2:CHARARRAY,
	f3:INT);

y = FOREACH x GENERATE f3;
z = ORDER y BY f3;
w = LIMIT z 5;

STORE w INTO 'output';


