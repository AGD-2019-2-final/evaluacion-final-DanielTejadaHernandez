-- 
-- Pregunta
-- ===========================================================================
-- 
-- Para el archivo `data.tsv` compute la cantidad de registros por letra. 
-- Escriba el resultado a la carpeta `output` del directorio actual.
--
fs -rm -f -r output;
--
-- >>> Escriba su respuesta a partir de este punto <<<
--

x = LOAD 'data.tsv'
    AS (f1:CHARARRAY,
	f2:CHARARRAY,
	f3:INT);

y = GROUP x BY f1;
z = FOREACH y GENERATE group, COUNT($1);

STORE z INTO 'output';

