-- 
-- Pregunta
-- ===========================================================================
-- 
-- Para el archivo `data.tsv` Calcule la cantidad de registros por clave de la 
-- columna 3. En otras palabras, cuántos registros hay que tengan la clave 
-- `aaa`?
-- 
-- Escriba el resultado a la carpeta `output` del directorio actual.
-- 
fs -rm -f -r output;
--
-- >>> Escriba su respuesta a partir de este punto <<<
--
w = LOAD 'data.tsv' USING PigStorage('\t')
    AS (f1:INT,
	f2:CHARARRAY,
	f3:MAP[]);

x= FOREACH w GENERATE FLATTEN(f3) AS (f1:CHARARRAY);
y = GROUP x BY f1;
z = FOREACH y GENERATE group, COUNT($1);
STORE z INTO 'output' USING PigStorage (',');
