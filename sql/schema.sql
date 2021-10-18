--Schema for cryptocurrency analysis
DROP TABLE IF EXISTS "currency_info";
CREATE TABLE "currency_info"(
   currency_code   VARCHAR (10),
   currency        TEXT
);

--Schema for crypto_prices table
DROP TABLE IF EXISTS "crypto_prices";
CREATE TABLE "crypto_prices"(
   time            TIMESTAMP WITH TIME ZONE NOT NULL,
   opening_price   DOUBLE PRECISION,
   highest_price   DOUBLE PRECISION,
   lowest_price    DOUBLE PRECISION,
   closing_price   DOUBLE PRECISION,
   volume_crypto   DOUBLE PRECISION,
   volume_btc      DOUBLE PRECISION,
   currency_code   VARCHAR (10)
);

SELECT create_hypertable('crypto_prices', 'time');