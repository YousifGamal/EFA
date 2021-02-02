--
-- PostgreSQL database dump
--

-- Dumped from database version 13.1 (Ubuntu 13.1-1.pgdg18.04+1)
-- Dumped by pg_dump version 13.1 (Ubuntu 13.1-1.pgdg18.04+1)

-- Started on 2021-02-02 20:23:02 EET

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
-- TOC entry 5 (class 2615 OID 24707)
-- Name: efa; Type: SCHEMA; Schema: -; Owner: postgres
--

CREATE SCHEMA efa;


ALTER SCHEMA efa OWNER TO postgres;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 202 (class 1259 OID 24710)
-- Name: linesman; Type: TABLE; Schema: efa; Owner: postgres
--

CREATE TABLE efa.linesman (
    linesman_id integer NOT NULL,
    linesman_name character varying(50) NOT NULL
);


ALTER TABLE efa.linesman OWNER TO postgres;

--
-- TOC entry 201 (class 1259 OID 24708)
-- Name: linesman_linesman_id_seq; Type: SEQUENCE; Schema: efa; Owner: postgres
--

CREATE SEQUENCE efa.linesman_linesman_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE efa.linesman_linesman_id_seq OWNER TO postgres;

--
-- TOC entry 3044 (class 0 OID 0)
-- Dependencies: 201
-- Name: linesman_linesman_id_seq; Type: SEQUENCE OWNED BY; Schema: efa; Owner: postgres
--

ALTER SEQUENCE efa.linesman_linesman_id_seq OWNED BY efa.linesman.linesman_id;


--
-- TOC entry 204 (class 1259 OID 24716)
-- Name: match; Type: TABLE; Schema: efa; Owner: postgres
--

CREATE TABLE efa.match (
    match_id integer NOT NULL,
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
-- TOC entry 203 (class 1259 OID 24714)
-- Name: match_match_id_seq; Type: SEQUENCE; Schema: efa; Owner: postgres
--

CREATE SEQUENCE efa.match_match_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE efa.match_match_id_seq OWNER TO postgres;

--
-- TOC entry 3045 (class 0 OID 0)
-- Dependencies: 203
-- Name: match_match_id_seq; Type: SEQUENCE OWNED BY; Schema: efa; Owner: postgres
--

ALTER SEQUENCE efa.match_match_id_seq OWNED BY efa.match.match_id;


--
-- TOC entry 206 (class 1259 OID 24723)
-- Name: referee; Type: TABLE; Schema: efa; Owner: postgres
--

CREATE TABLE efa.referee (
    referee_id integer NOT NULL,
    referee_name character varying(50) NOT NULL
);


ALTER TABLE efa.referee OWNER TO postgres;

--
-- TOC entry 205 (class 1259 OID 24721)
-- Name: referee_referee_id_seq; Type: SEQUENCE; Schema: efa; Owner: postgres
--

CREATE SEQUENCE efa.referee_referee_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE efa.referee_referee_id_seq OWNER TO postgres;

--
-- TOC entry 3046 (class 0 OID 0)
-- Dependencies: 205
-- Name: referee_referee_id_seq; Type: SEQUENCE OWNED BY; Schema: efa; Owner: postgres
--

ALTER SEQUENCE efa.referee_referee_id_seq OWNED BY efa.referee.referee_id;


--
-- TOC entry 208 (class 1259 OID 24729)
-- Name: reservation; Type: TABLE; Schema: efa; Owner: postgres
--

CREATE TABLE efa.reservation (
    ticket_number integer NOT NULL,
    user_id integer NOT NULL,
    match_id integer NOT NULL,
    seat_number integer NOT NULL
);


ALTER TABLE efa.reservation OWNER TO postgres;

--
-- TOC entry 207 (class 1259 OID 24727)
-- Name: reservation_ticket_number_seq; Type: SEQUENCE; Schema: efa; Owner: postgres
--

CREATE SEQUENCE efa.reservation_ticket_number_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE efa.reservation_ticket_number_seq OWNER TO postgres;

--
-- TOC entry 3047 (class 0 OID 0)
-- Dependencies: 207
-- Name: reservation_ticket_number_seq; Type: SEQUENCE OWNED BY; Schema: efa; Owner: postgres
--

ALTER SEQUENCE efa.reservation_ticket_number_seq OWNED BY efa.reservation.ticket_number;


--
-- TOC entry 210 (class 1259 OID 24735)
-- Name: stadium; Type: TABLE; Schema: efa; Owner: postgres
--

CREATE TABLE efa.stadium (
    stadium_id integer NOT NULL,
    stadium_name character varying(50) NOT NULL,
    rows integer NOT NULL,
    columns integer NOT NULL
);


ALTER TABLE efa.stadium OWNER TO postgres;

--
-- TOC entry 209 (class 1259 OID 24733)
-- Name: stadium_stadium_id_seq; Type: SEQUENCE; Schema: efa; Owner: postgres
--

CREATE SEQUENCE efa.stadium_stadium_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE efa.stadium_stadium_id_seq OWNER TO postgres;

--
-- TOC entry 3048 (class 0 OID 0)
-- Dependencies: 209
-- Name: stadium_stadium_id_seq; Type: SEQUENCE OWNED BY; Schema: efa; Owner: postgres
--

ALTER SEQUENCE efa.stadium_stadium_id_seq OWNED BY efa.stadium.stadium_id;


--
-- TOC entry 212 (class 1259 OID 24741)
-- Name: teams; Type: TABLE; Schema: efa; Owner: postgres
--

CREATE TABLE efa.teams (
    team_id integer NOT NULL,
    team_name character varying(50) NOT NULL
);


ALTER TABLE efa.teams OWNER TO postgres;

--
-- TOC entry 211 (class 1259 OID 24739)
-- Name: teams_team_id_seq; Type: SEQUENCE; Schema: efa; Owner: postgres
--

CREATE SEQUENCE efa.teams_team_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE efa.teams_team_id_seq OWNER TO postgres;

--
-- TOC entry 3049 (class 0 OID 0)
-- Dependencies: 211
-- Name: teams_team_id_seq; Type: SEQUENCE OWNED BY; Schema: efa; Owner: postgres
--

ALTER SEQUENCE efa.teams_team_id_seq OWNED BY efa.teams.team_id;


--
-- TOC entry 214 (class 1259 OID 24747)
-- Name: user; Type: TABLE; Schema: efa; Owner: postgres
--

CREATE TABLE efa."user" (
    user_id integer NOT NULL,
    user_name character varying(50) NOT NULL,
    password character varying(50) NOT NULL,
    first_name character varying(50) NOT NULL,
    last_name character varying(50) NOT NULL,
    birth_date date NOT NULL,
    gender "char" NOT NULL,
    city character varying(50) NOT NULL,
    address text,
    email character varying(50) NOT NULL,
    role "char" NOT NULL,
    status integer NOT NULL
);


ALTER TABLE efa."user" OWNER TO postgres;

--
-- TOC entry 213 (class 1259 OID 24745)
-- Name: user_user_id_seq; Type: SEQUENCE; Schema: efa; Owner: postgres
--

CREATE SEQUENCE efa.user_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE efa.user_user_id_seq OWNER TO postgres;

--
-- TOC entry 3050 (class 0 OID 0)
-- Dependencies: 213
-- Name: user_user_id_seq; Type: SEQUENCE OWNED BY; Schema: efa; Owner: postgres
--

ALTER SEQUENCE efa.user_user_id_seq OWNED BY efa."user".user_id;


--
-- TOC entry 2867 (class 2604 OID 24713)
-- Name: linesman linesman_id; Type: DEFAULT; Schema: efa; Owner: postgres
--

ALTER TABLE ONLY efa.linesman ALTER COLUMN linesman_id SET DEFAULT nextval('efa.linesman_linesman_id_seq'::regclass);


--
-- TOC entry 2868 (class 2604 OID 24719)
-- Name: match match_id; Type: DEFAULT; Schema: efa; Owner: postgres
--

ALTER TABLE ONLY efa.match ALTER COLUMN match_id SET DEFAULT nextval('efa.match_match_id_seq'::regclass);


--
-- TOC entry 2870 (class 2604 OID 24726)
-- Name: referee referee_id; Type: DEFAULT; Schema: efa; Owner: postgres
--

ALTER TABLE ONLY efa.referee ALTER COLUMN referee_id SET DEFAULT nextval('efa.referee_referee_id_seq'::regclass);


--
-- TOC entry 2871 (class 2604 OID 24732)
-- Name: reservation ticket_number; Type: DEFAULT; Schema: efa; Owner: postgres
--

ALTER TABLE ONLY efa.reservation ALTER COLUMN ticket_number SET DEFAULT nextval('efa.reservation_ticket_number_seq'::regclass);


--
-- TOC entry 2872 (class 2604 OID 24738)
-- Name: stadium stadium_id; Type: DEFAULT; Schema: efa; Owner: postgres
--

ALTER TABLE ONLY efa.stadium ALTER COLUMN stadium_id SET DEFAULT nextval('efa.stadium_stadium_id_seq'::regclass);


--
-- TOC entry 2873 (class 2604 OID 24744)
-- Name: teams team_id; Type: DEFAULT; Schema: efa; Owner: postgres
--

ALTER TABLE ONLY efa.teams ALTER COLUMN team_id SET DEFAULT nextval('efa.teams_team_id_seq'::regclass);


--
-- TOC entry 2874 (class 2604 OID 24750)
-- Name: user user_id; Type: DEFAULT; Schema: efa; Owner: postgres
--

ALTER TABLE ONLY efa."user" ALTER COLUMN user_id SET DEFAULT nextval('efa.user_user_id_seq'::regclass);


--
-- TOC entry 2876 (class 2606 OID 24755)
-- Name: linesman linesman_pkey; Type: CONSTRAINT; Schema: efa; Owner: postgres
--

ALTER TABLE ONLY efa.linesman
    ADD CONSTRAINT linesman_pkey PRIMARY KEY (linesman_id);


--
-- TOC entry 2884 (class 2606 OID 24757)
-- Name: match match_pkey; Type: CONSTRAINT; Schema: efa; Owner: postgres
--

ALTER TABLE ONLY efa.match
    ADD CONSTRAINT match_pkey PRIMARY KEY (match_id);


--
-- TOC entry 2886 (class 2606 OID 24759)
-- Name: referee referee_pkey; Type: CONSTRAINT; Schema: efa; Owner: postgres
--

ALTER TABLE ONLY efa.referee
    ADD CONSTRAINT referee_pkey PRIMARY KEY (referee_id);


--
-- TOC entry 2888 (class 2606 OID 24820)
-- Name: reservation reservation_match_id_seat_number_key; Type: CONSTRAINT; Schema: efa; Owner: postgres
--

ALTER TABLE ONLY efa.reservation
    ADD CONSTRAINT reservation_match_id_seat_number_key UNIQUE (match_id, seat_number);


--
-- TOC entry 2890 (class 2606 OID 24761)
-- Name: reservation reservation_pkey; Type: CONSTRAINT; Schema: efa; Owner: postgres
--

ALTER TABLE ONLY efa.reservation
    ADD CONSTRAINT reservation_pkey PRIMARY KEY (ticket_number);


--
-- TOC entry 2892 (class 2606 OID 24763)
-- Name: reservation reservation_user_id_match_id_seat_number_key; Type: CONSTRAINT; Schema: efa; Owner: postgres
--

ALTER TABLE ONLY efa.reservation
    ADD CONSTRAINT reservation_user_id_match_id_seat_number_key UNIQUE (user_id, match_id, seat_number);


--
-- TOC entry 2894 (class 2606 OID 24765)
-- Name: stadium stadium_pkey; Type: CONSTRAINT; Schema: efa; Owner: postgres
--

ALTER TABLE ONLY efa.stadium
    ADD CONSTRAINT stadium_pkey PRIMARY KEY (stadium_id);


--
-- TOC entry 2896 (class 2606 OID 24767)
-- Name: stadium stadium_stadium_name_key; Type: CONSTRAINT; Schema: efa; Owner: postgres
--

ALTER TABLE ONLY efa.stadium
    ADD CONSTRAINT stadium_stadium_name_key UNIQUE (stadium_name);


--
-- TOC entry 2898 (class 2606 OID 24769)
-- Name: teams teams_pkey; Type: CONSTRAINT; Schema: efa; Owner: postgres
--

ALTER TABLE ONLY efa.teams
    ADD CONSTRAINT teams_pkey PRIMARY KEY (team_id);


--
-- TOC entry 2900 (class 2606 OID 24771)
-- Name: user user_pkey; Type: CONSTRAINT; Schema: efa; Owner: postgres
--

ALTER TABLE ONLY efa."user"
    ADD CONSTRAINT user_pkey PRIMARY KEY (user_id);


--
-- TOC entry 2877 (class 1259 OID 24772)
-- Name: fk_away_team; Type: INDEX; Schema: efa; Owner: postgres
--

CREATE INDEX fk_away_team ON efa.match USING btree (away_team);


--
-- TOC entry 2878 (class 1259 OID 24773)
-- Name: fk_home_team; Type: INDEX; Schema: efa; Owner: postgres
--

CREATE INDEX fk_home_team ON efa.match USING btree (home_team);


--
-- TOC entry 2879 (class 1259 OID 24774)
-- Name: fk_linesman_1; Type: INDEX; Schema: efa; Owner: postgres
--

CREATE INDEX fk_linesman_1 ON efa.match USING btree (linesman_1);


--
-- TOC entry 2880 (class 1259 OID 24775)
-- Name: fk_linesman_2; Type: INDEX; Schema: efa; Owner: postgres
--

CREATE INDEX fk_linesman_2 ON efa.match USING btree (linesman_2);


--
-- TOC entry 2881 (class 1259 OID 24776)
-- Name: fk_referee; Type: INDEX; Schema: efa; Owner: postgres
--

CREATE INDEX fk_referee ON efa.match USING btree (main_referee);


--
-- TOC entry 2882 (class 1259 OID 24777)
-- Name: fk_stadium; Type: INDEX; Schema: efa; Owner: postgres
--

CREATE INDEX fk_stadium ON efa.match USING btree (stadium_id);


--
-- TOC entry 2901 (class 2606 OID 24778)
-- Name: match match_away_team_fkey; Type: FK CONSTRAINT; Schema: efa; Owner: postgres
--

ALTER TABLE ONLY efa.match
    ADD CONSTRAINT match_away_team_fkey FOREIGN KEY (away_team) REFERENCES efa.teams(team_id);


--
-- TOC entry 2902 (class 2606 OID 24783)
-- Name: match match_home_team_fkey; Type: FK CONSTRAINT; Schema: efa; Owner: postgres
--

ALTER TABLE ONLY efa.match
    ADD CONSTRAINT match_home_team_fkey FOREIGN KEY (home_team) REFERENCES efa.teams(team_id);


--
-- TOC entry 2903 (class 2606 OID 24788)
-- Name: match match_linesman_1_fkey; Type: FK CONSTRAINT; Schema: efa; Owner: postgres
--

ALTER TABLE ONLY efa.match
    ADD CONSTRAINT match_linesman_1_fkey FOREIGN KEY (linesman_1) REFERENCES efa.linesman(linesman_id);


--
-- TOC entry 2904 (class 2606 OID 24793)
-- Name: match match_linesman_2_fkey; Type: FK CONSTRAINT; Schema: efa; Owner: postgres
--

ALTER TABLE ONLY efa.match
    ADD CONSTRAINT match_linesman_2_fkey FOREIGN KEY (linesman_2) REFERENCES efa.linesman(linesman_id);


--
-- TOC entry 2905 (class 2606 OID 24798)
-- Name: match match_main_referee_fkey; Type: FK CONSTRAINT; Schema: efa; Owner: postgres
--

ALTER TABLE ONLY efa.match
    ADD CONSTRAINT match_main_referee_fkey FOREIGN KEY (main_referee) REFERENCES efa.referee(referee_id);


--
-- TOC entry 2906 (class 2606 OID 24803)
-- Name: match match_stadium_id_fkey; Type: FK CONSTRAINT; Schema: efa; Owner: postgres
--

ALTER TABLE ONLY efa.match
    ADD CONSTRAINT match_stadium_id_fkey FOREIGN KEY (stadium_id) REFERENCES efa.stadium(stadium_id);


--
-- TOC entry 2907 (class 2606 OID 24808)
-- Name: reservation reservation_match_id_fkey; Type: FK CONSTRAINT; Schema: efa; Owner: postgres
--

ALTER TABLE ONLY efa.reservation
    ADD CONSTRAINT reservation_match_id_fkey FOREIGN KEY (match_id) REFERENCES efa.match(match_id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 2908 (class 2606 OID 24813)
-- Name: reservation reservation_user_id_fkey; Type: FK CONSTRAINT; Schema: efa; Owner: postgres
--

ALTER TABLE ONLY efa.reservation
    ADD CONSTRAINT reservation_user_id_fkey FOREIGN KEY (user_id) REFERENCES efa."user"(user_id) ON UPDATE CASCADE ON DELETE CASCADE;


-- Completed on 2021-02-02 20:23:02 EET

--
-- PostgreSQL database dump complete
--

