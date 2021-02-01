--
-- PostgreSQL database dump
--

-- Dumped from database version 13.1 (Ubuntu 13.1-1.pgdg18.04+1)
-- Dumped by pg_dump version 13.1 (Ubuntu 13.1-1.pgdg18.04+1)

-- Started on 2021-01-30 19:58:47 EET

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 6 (class 2615 OID 16385)
-- Name: efa; Type: SCHEMA; Schema: -; Owner: postgres
--

CREATE SCHEMA efa;


ALTER SCHEMA efa OWNER TO postgres;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 207 (class 1259 OID 16448)
-- Name: linesman; Type: TABLE; Schema: efa; Owner: postgres
--


CREATE TABLE efa.linesman (
    linesman_id  SERIAL,
    linesman_name varchar(50) NOT NULL
);


ALTER TABLE efa.linesman OWNER TO postgres;

--
-- TOC entry 202 (class 1259 OID 16394)
-- Name: match; Type: TABLE; Schema: efa; Owner: postgres
--

CREATE TABLE efa.match (
    match_id  SERIAL,
    stadium_id integer NOT NULL,
    home_team integer NOT NULL,
    away_team integer NOT NULL,
    main_referee integer NOT NULL,
    linesman_1 integer NOT NULL,
    linesman_2 integer NOT NULL,
    mdate date NOT NULL,
    mtime time without time zone NOT NULL,
    CONSTRAINT linesmen CHECK ((linesman_1 <> linesman_2))
);


ALTER TABLE efa.match OWNER TO postgres;

--
-- TOC entry 206 (class 1259 OID 16440)
-- Name: referee; Type: TABLE; Schema: efa; Owner: postgres
--

CREATE TABLE efa.referee (
    referee_id  SERIAL,
    referee_name varchar(50) NOT NULL
);


ALTER TABLE efa.referee OWNER TO postgres;

--
-- TOC entry 203 (class 1259 OID 16402)
-- Name: reservation; Type: TABLE; Schema: efa; Owner: postgres
--

CREATE TABLE efa.reservation (
    ticket_number varchar(50) NOT NULL,
    user_id integer NOT NULL,
    match_id integer NOT NULL,
    seat_number integer NOT NULL
);


ALTER TABLE efa.reservation OWNER TO postgres;

--
-- TOC entry 204 (class 1259 OID 16422)
-- Name: stadium; Type: TABLE; Schema: efa; Owner: postgres
--

CREATE TABLE efa.stadium (
    stadium_id SERIAL,
    stadium_name varchar(50) NOT NULL,
    rows integer NOT NULL,
    columns integer NOT NULL
);


ALTER TABLE efa.stadium OWNER TO postgres;

--
-- TOC entry 205 (class 1259 OID 16432)
-- Name: teams; Type: TABLE; Schema: efa; Owner: postgres
--

CREATE TABLE efa.teams (
    team_id  SERIAL,
    team_name varchar(50) NOT NULL
);


ALTER TABLE efa.teams OWNER TO postgres;

--
-- TOC entry 201 (class 1259 OID 16386)
-- Name: user; Type: TABLE; Schema: efa; Owner: postgres
--

CREATE TABLE efa."user" (
    user_id  SERIAL,
    user_name varchar(50) NOT NULL,
    password varchar(50) NOT NULL,
    first_name varchar(50) NOT NULL,
    last_name varchar(50) NOT NULL,
    birth_date date NOT NULL,
    gender "char" NOT NULL,
    city varchar(50) NOT NULL,
    address text,
    email varchar(50) NOT NULL,
    role "char" NOT NULL,
    status integer NOT NULL
);


ALTER TABLE efa."user" OWNER TO postgres;

--
-- TOC entry 2884 (class 2606 OID 16455)
-- Name: linesman linesman_pkey; Type: CONSTRAINT; Schema: efa; Owner: postgres
--

ALTER TABLE ONLY efa.linesman
    ADD CONSTRAINT linesman_pkey PRIMARY KEY (linesman_id);


--
-- TOC entry 2870 (class 2606 OID 16399)
-- Name: match match_pkey; Type: CONSTRAINT; Schema: efa; Owner: postgres
--

ALTER TABLE ONLY efa.match
    ADD CONSTRAINT match_pkey PRIMARY KEY (match_id);


--
-- TOC entry 2882 (class 2606 OID 16447)
-- Name: referee referee_pkey; Type: CONSTRAINT; Schema: efa; Owner: postgres
--

ALTER TABLE ONLY efa.referee
    ADD CONSTRAINT referee_pkey PRIMARY KEY (referee_id);


--
-- TOC entry 2872 (class 2606 OID 16409)
-- Name: reservation reservation_pkey; Type: CONSTRAINT; Schema: efa; Owner: postgres
--

ALTER TABLE ONLY efa.reservation
    ADD CONSTRAINT reservation_pkey PRIMARY KEY (ticket_number);


--
-- TOC entry 2874 (class 2606 OID 16421)
-- Name: reservation reservation_user_id_match_id_seat_number_key; Type: CONSTRAINT; Schema: efa; Owner: postgres
--

ALTER TABLE ONLY efa.reservation
    ADD CONSTRAINT reservation_user_id_match_id_seat_number_key UNIQUE (user_id, match_id, seat_number);


--
-- TOC entry 2876 (class 2606 OID 16429)
-- Name: stadium stadium_pkey; Type: CONSTRAINT; Schema: efa; Owner: postgres
--

ALTER TABLE ONLY efa.stadium
    ADD CONSTRAINT stadium_pkey PRIMARY KEY (stadium_id);


--
-- TOC entry 2878 (class 2606 OID 16431)
-- Name: stadium stadium_stadium_name_key; Type: CONSTRAINT; Schema: efa; Owner: postgres
--

ALTER TABLE ONLY efa.stadium
    ADD CONSTRAINT stadium_stadium_name_key UNIQUE (stadium_name);


--
-- TOC entry 2880 (class 2606 OID 16439)
-- Name: teams teams_pkey; Type: CONSTRAINT; Schema: efa; Owner: postgres
--

ALTER TABLE ONLY efa.teams
    ADD CONSTRAINT teams_pkey PRIMARY KEY (team_id);


--
-- TOC entry 2862 (class 2606 OID 16393)
-- Name: user user_pkey; Type: CONSTRAINT; Schema: efa; Owner: postgres
--

ALTER TABLE ONLY efa."user"
    ADD CONSTRAINT user_pkey PRIMARY KEY (user_id);


--
-- TOC entry 2863 (class 1259 OID 16473)
-- Name: fk_away_team; Type: INDEX; Schema: efa; Owner: postgres
--

CREATE INDEX fk_away_team ON efa.match USING btree (away_team);


--
-- TOC entry 2864 (class 1259 OID 16461)
-- Name: fk_home_team; Type: INDEX; Schema: efa; Owner: postgres
--

CREATE INDEX fk_home_team ON efa.match USING btree (home_team);


--
-- TOC entry 2865 (class 1259 OID 16485)
-- Name: fk_linesman_1; Type: INDEX; Schema: efa; Owner: postgres
--

CREATE INDEX fk_linesman_1 ON efa.match USING btree (linesman_1);


--
-- TOC entry 2866 (class 1259 OID 16491)
-- Name: fk_linesman_2; Type: INDEX; Schema: efa; Owner: postgres
--

CREATE INDEX fk_linesman_2 ON efa.match USING btree (linesman_2);


--
-- TOC entry 2867 (class 1259 OID 16479)
-- Name: fk_referee; Type: INDEX; Schema: efa; Owner: postgres
--

CREATE INDEX fk_referee ON efa.match USING btree (main_referee);


--
-- TOC entry 2868 (class 1259 OID 16467)
-- Name: fk_stadium; Type: INDEX; Schema: efa; Owner: postgres
--

CREATE INDEX fk_stadium ON efa.match USING btree (stadium_id);


--
-- TOC entry 2887 (class 2606 OID 16468)
-- Name: match match_away_team_fkey; Type: FK CONSTRAINT; Schema: efa; Owner: postgres
--

ALTER TABLE ONLY efa.match
    ADD CONSTRAINT match_away_team_fkey FOREIGN KEY (away_team) REFERENCES efa.teams(team_id);


--
-- TOC entry 2885 (class 2606 OID 16456)
-- Name: match match_home_team_fkey; Type: FK CONSTRAINT; Schema: efa; Owner: postgres
--

ALTER TABLE ONLY efa.match
    ADD CONSTRAINT match_home_team_fkey FOREIGN KEY (home_team) REFERENCES efa.teams(team_id);


--
-- TOC entry 2888 (class 2606 OID 16480)
-- Name: match match_linesman_1_fkey; Type: FK CONSTRAINT; Schema: efa; Owner: postgres
--

ALTER TABLE ONLY efa.match
    ADD CONSTRAINT match_linesman_1_fkey FOREIGN KEY (linesman_1) REFERENCES efa.linesman(linesman_id);


--
-- TOC entry 2889 (class 2606 OID 16486)
-- Name: match match_linesman_2_fkey; Type: FK CONSTRAINT; Schema: efa; Owner: postgres
--

ALTER TABLE ONLY efa.match
    ADD CONSTRAINT match_linesman_2_fkey FOREIGN KEY (linesman_2) REFERENCES efa.linesman(linesman_id);


--
-- TOC entry 2890 (class 2606 OID 16474)
-- Name: match match_main_referee_fkey; Type: FK CONSTRAINT; Schema: efa; Owner: postgres
--

ALTER TABLE ONLY efa.match
    ADD CONSTRAINT match_main_referee_fkey FOREIGN KEY (main_referee) REFERENCES efa.referee(referee_id);


--
-- TOC entry 2886 (class 2606 OID 16462)
-- Name: match match_stadium_id_fkey; Type: FK CONSTRAINT; Schema: efa; Owner: postgres
--

ALTER TABLE ONLY efa.match
    ADD CONSTRAINT match_stadium_id_fkey FOREIGN KEY (stadium_id) REFERENCES efa.stadium(stadium_id);


--
-- TOC entry 2892 (class 2606 OID 16415)
-- Name: reservation reservation_match_id_fkey; Type: FK CONSTRAINT; Schema: efa; Owner: postgres
--

ALTER TABLE ONLY efa.reservation
    ADD CONSTRAINT reservation_match_id_fkey FOREIGN KEY (match_id) REFERENCES efa.match(match_id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 2891 (class 2606 OID 16410)
-- Name: reservation reservation_user_id_fkey; Type: FK CONSTRAINT; Schema: efa; Owner: postgres
--

ALTER TABLE ONLY efa.reservation
    ADD CONSTRAINT reservation_user_id_fkey FOREIGN KEY (user_id) REFERENCES efa."user"(user_id) ON UPDATE CASCADE ON DELETE CASCADE;


-- Completed on 2021-01-30 19:58:47 EET

--
-- PostgreSQL database dump complete
--

