"""
copy from pyomop cdm6
https://github.com/dermatologist/pyomop/blob/develop/src/pyomop/cdm6_tables.py

ORM - creating OMOP CDM v6.0 like objects with the help of sqlalchemy
"""

# coding: utf-8
from sqlalchemy import Column, Integer, Numeric, String, Text, MetaData
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class MetaData(Base):
    __tablename__ = "metadata"

    _id = Column(Integer, primary_key=True)
    metadata_concept_id = Column(Integer, nullable=False)
    metadata_type_concept_id = Column(Integer, nullable=False)
    name = Column(String(250))
    value_as_string = Column(String(250))
    value_as_concept_id = Column(Integer)
    metadata_date = Column(String(30))
    metadata_datetime = Column(String(10))


class CareSite(Base):
    __tablename__ = "care_site"

    # _id = Column(Integer, primary_key=True)
    care_site_id = Column(Integer, primary_key=True)
    care_site_name = Column(String(255))
    place_of_service_concept_id = Column(Integer, nullable=False)
    location_id = Column(Integer)
    care_site_source_value = Column(String(50))
    place_of_service_source_value = Column(String(50))


class CdmSource(Base):
    __tablename__ = "cdm_source"

    # _id = Column(Integer, primary_key=True)
    cdm_source_name = Column(String(255), primary_key=True)
    cdm_source_abbreviation = Column(String(25))
    cdm_holder = Column(String(255))
    source_description = Column(Text)
    source_documentation_reference = Column(String(255))
    cdm_etl_reference = Column(String(255))
    source_release_date = Column(String(30))
    cdm_release_date = Column(String(30))
    cdm_version = Column(String(10))
    vocabulary_version = Column(String(20))


class Cost(Base):
    __tablename__ = "cost"

    cost_id = Column(Integer, primary_key=True)
    person_id = Column(Integer, nullable=False)
    cost_event_id = Column(Integer, nullable=False)
    cost_event_field_concept_id = Column(Integer, nullable=False)
    cost_concept_id = Column(Integer)
    cost_type_concept_id = Column(Integer)
    cost_source_concept_id = Column(Integer)
    cost_source_value = Column(String(50))
    currency_concept_id = Column(Integer)
    cost = Column(Numeric)
    incurred_date = Column(String(30))
    billed_date = Column(String(30))
    paid_date = Column(String(30))
    revenue_code_concept_id = Column(Integer)
    drg_concept_id = Column(Integer)
    revenue_code_source_value = Column(String(50))
    drg_source_value = Column(String(50))
    payer_plan_period_id = Column(Integer)


class Cohort(Base):
    __tablename__ = "cohort"

    _id = Column(Integer, primary_key=True)
    cohort_definition_id = Column(Integer, nullable=False)
    subject_id = Column(Integer, nullable=False)
    cohort_start_date = Column(String(30), nullable=False)
    cohort_end_date = Column(String(30), nullable=False)


class CohortDefinition(Base):
    __tablename__ = "cohort_definition"

    _id = Column(Integer, primary_key=True)
    cohort_definition_id = Column(Integer, nullable=False)
    cohort_definition_name = Column(String(255), nullable=False)
    cohort_definition_description = Column(Text)
    definition_type_concept_id = Column(Integer, nullable=False)
    cohort_definition_syntax = Column(Text)
    subject_concept_id = Column(Integer, nullable=False)
    cohort_initiation_date = Column(String(30))


class Concept(Base):
    __tablename__ = "concept"

    # _id = Column(Integer, primary_key=True)
    concept_id = Column(Integer, primary_key=True)
    concept_name = Column(String(255), nullable=False)
    domain_id = Column(String(20), nullable=False)
    vocabulary_id = Column(String(20), nullable=False)
    concept_class_id = Column(String(20), nullable=False)
    standard_concept = Column(String(1))
    concept_code = Column(String(50), nullable=False)
    valid_start_date = Column(String(30), nullable=False)
    valid_end_date = Column(String(30), nullable=False)
    invalid_reason = Column(String(1))


class ConceptAncestor(Base):
    __tablename__ = "concept_ancestor"

    _id = Column(Integer, primary_key=True)
    ancestor_concept_id = Column(Integer, nullable=False)
    descendant_concept_id = Column(Integer, nullable=False)
    min_levels_of_separation = Column(Integer, nullable=False)
    max_levels_of_separation = Column(Integer, nullable=False)


class ConceptClass(Base):
    __tablename__ = "concept_class"

    # _id = Column(Integer, primary_key=True)
    concept_class_id = Column(String(20), primary_key=True)
    concept_class_name = Column(String(255), nullable=False)
    concept_class_concept_id = Column(Integer, nullable=False)


class ConceptRelationship(Base):
    __tablename__ = "concept_relationship"

    _id = Column(Integer, primary_key=True)
    concept_id_1 = Column(Integer, nullable=False)
    concept_id_2 = Column(Integer, nullable=False)
    relationship_id = Column(String(20), nullable=False)
    valid_start_date = Column(String(30), nullable=False)
    valid_end_date = Column(String(30), nullable=False)
    invalid_reason = Column(String(1))


class ConceptSynonym(Base):
    __tablename__ = "concept_synonym"

    _id = Column(Integer, primary_key=True)
    concept_id = Column(Integer, nullable=False)
    concept_synonym_name = Column(String(1000), nullable=False)
    language_concept_id = Column(Integer, nullable=False)


class ConditionEra(Base):
    __tablename__ = "condition_era"

    # _id = Column(Integer, primary_key=True)
    condition_era_id = Column(Integer, primary_key=True)
    person_id = Column(Integer, nullable=False)
    condition_concept_id = Column(Integer, nullable=False)
    condition_era_start_datetime = Column(String(10), nullable=False)
    condition_era_end_datetime = Column(String(10), nullable=False)
    condition_occurrence_count = Column(Integer)


class ConditionOccurrence(Base):
    __tablename__ = "condition_occurrence"

    # _id = Column(Integer, primary_key=True)
    condition_occurrence_id = Column(Integer, primary_key=True)
    person_id = Column(Integer, nullable=False)
    condition_concept_id = Column(Integer, nullable=False)
    condition_start_date = Column(String(30), nullable=False)
    condition_start_datetime = Column(String(10))
    condition_end_date = Column(String(30))
    condition_end_datetime = Column(String(10))
    condition_type_concept_id = Column(Integer, nullable=False)
    condition_status_concept_id = Column(Integer, nullable=False)
    stop_reason = Column(String(20))
    provider_id = Column(Integer)
    visit_occurrence_id = Column(Integer)
    visit_detail_id = Column(Integer)
    condition_source_value = Column(String(50))
    condition_source_concept_id = Column(Integer, nullable=False)
    condition_status_source_value = Column(String(50))


class DeviceExposure(Base):
    __tablename__ = "device_exposure"

    # _id = Column(Integer, primary_key=True)
    device_exposure_id = Column(Integer, primary_key=True)
    person_id = Column(Integer, nullable=False)
    device_concept_id = Column(Integer, nullable=False)
    device_exposure_start_date = Column(String(30), nullable=False)
    device_exposure_start_datetime = Column(String(10))
    device_exposure_end_date = Column(String(30))
    device_exposure_end_datetime = Column(String(10))
    device_type_concept_id = Column(Integer, nullable=False)
    unique_device_id = Column(String(50))
    quantity = Column(Integer)
    provider_id = Column(Integer)
    visit_occurrence_id = Column(Integer)
    visit_detail_id = Column(Integer)
    device_source_value = Column(String(50))
    device_source_concept_id = Column(Integer, nullable=False)


class Domain(Base):
    __tablename__ = "domain"

    # _id = Column(Integer, primary_key=True, nullable=False)
    domain_id = Column(String(20), primary_key=True)
    domain_name = Column(String(255), nullable=False)
    domain_concept_id = Column(Integer, nullable=False)


class DoseEra(Base):
    __tablename__ = "dose_era"

    # _id = Column(Integer, primary_key=True)
    dose_era_id = Column(Integer, primary_key=True)
    person_id = Column(Integer, nullable=False)
    drug_concept_id = Column(Integer, nullable=False)
    unit_concept_id = Column(Integer, nullable=False)
    dose_value = Column(Numeric, nullable=False)
    dose_era_start_datetime = Column(String(10), nullable=False)
    dose_era_end_datetime = Column(String(10), nullable=False)


class DrugEra(Base):
    __tablename__ = "drug_era"

    # _id = Column(Integer, primary_key=True)
    drug_era_id = Column(Integer, primary_key=True)
    person_id = Column(Integer, nullable=False)
    drug_concept_id = Column(Integer, nullable=False)
    drug_era_start_datetime = Column(String(10), nullable=False)
    drug_era_end_datetime = Column(String(10), nullable=False)
    drug_exposure_count = Column(Integer)
    gap_days = Column(Integer)


class DrugExposure(Base):
    __tablename__ = "drug_exposure"

    # _id = Column(Integer, primary_key=True)
    drug_exposure_id = Column(Integer, primary_key=True)
    person_id = Column(Integer, nullable=False)
    drug_concept_id = Column(Integer, nullable=False)
    drug_exposure_start_date = Column(String(30), nullable=False)
    drug_exposure_start_datetime = Column(String(10))
    drug_exposure_end_date = Column(String(30), nullable=False)
    drug_exposure_end_datetime = Column(String(10))
    verbatim_end_date = Column(String(30))
    drug_type_concept_id = Column(Integer, nullable=False)
    stop_reason = Column(String(20))
    refills = Column(Integer)
    quantity = Column(Numeric)
    days_supply = Column(Integer)
    sig = Column(Text)
    route_concept_id = Column(Integer)
    # effective_drug_dose = Column(Numeric)
    # dose_unit_concept_id = Column(Integer)
    lot_number = Column(String(50))
    provider_id = Column(Integer)
    visit_occurrence_id = Column(Integer)
    visit_detail_id = Column(Integer)
    drug_source_value = Column(String(50))
    drug_source_concept_id = Column(Integer, nullable=False)
    route_source_value = Column(String(50))
    dose_unit_source_value = Column(String(50))


class DrugStrength(Base):
    __tablename__ = "drug_strength"

    _id = Column(Integer, primary_key=True)
    drug_concept_id = Column(Integer, nullable=False)
    # drug_concept_id = Column(Integer, primary_key=True)
    ingredient_concept_id = Column(Integer, nullable=False)
    amount_value = Column(Numeric)
    amount_unit_concept_id = Column(Integer)
    numerator_value = Column(Numeric)
    numerator_unit_concept_id = Column(Integer)
    denominator_value = Column(Numeric)
    denominator_unit_concept_id = Column(Integer)
    box_size = Column(Integer)
    valid_start_date = Column(String(30), nullable=False)
    valid_end_date = Column(String(30), nullable=False)
    invalid_reason = Column(String(1))


class FactRelationship(Base):
    __tablename__ = "fact_relationship"

    _id = Column(Integer, primary_key=True)
    domain_concept_id_1 = Column(Integer, nullable=False)
    fact_id_1 = Column(Integer, nullable=False)
    domain_concept_id_2 = Column(Integer, nullable=False)
    fact_id_2 = Column(Integer, nullable=False)
    relationship_concept_id = Column(Integer, nullable=False)


class SurveyConduct(Base):
    __tablename__ = "survey_conduct"

    survey_conduct_id = Column(Integer, primary_key=True)
    person_id = Column(Integer, nullable=False)
    survey_concept_id = Column(Integer, nullable=False)
    survey_start_date = Column(String(30))
    survey_start_datetime = Column(String(10))
    survey_end_date = Column(String(30))
    survey_end_datetime = Column(String(10), nullable=False)
    provider_id = Column(Integer)
    assisted_concept_id = Column(Integer, nullable=False)
    respondent_type_concept_id = Column(Integer, nullable=False)
    timing_concept_id = Column(Integer, nullable=False)
    collection_method_concept_id = Column(Integer, nullable=False)
    assisted_source_value = Column(String(50))
    respondent_type_source_value = Column(String(100))
    timing_source_value = Column(String(100))
    collection_method_source_value = Column(String(100))
    survey_source_value = Column(String(100))
    survey_source_concept_id = Column(Integer, nullable=False)
    survey_source_identifier = Column(String(100))
    validated_survey_concept_id = Column(Integer, nullable=False)
    validated_survey_source_value = Column(Integer)
    survey_version_number = Column(String(20))
    visit_occurrence_id = Column(Integer)
    response_visit_occurrence_id = Column(Integer)


class Location(Base):
    __tablename__ = "location"

    # _id = Column(Integer, primary_key=True)
    location_id = Column(Integer, primary_key=True)
    address_1 = Column(String(50))
    address_2 = Column(String(50))
    city = Column(String(50))
    state = Column(String(2))
    zip = Column(String(9))
    county = Column(String(20))
    location_source_value = Column(String(50))
    latitude = Column(Numeric)
    longitude = Column(Numeric)


class LocationHistory(Base):
    __tablename__ = "location_history"

    location_id = Column(Integer, primary_key=True)
    relationship_type_concept_id = Column(Integer, nullable=True)
    domain_id = Column(String(50), nullable=True)
    entity_id = Column(Integer, nullable=False)
    start_date = Column(String(30), nullable=False)
    end_date = Column(String(30))


class Measurement(Base):
    __tablename__ = "measurement"

    # _id = Column(Integer, primary_key=True)
    measurement_id = Column(Integer, primary_key=True)
    person_id = Column(Integer, nullable=False)
    measurement_concept_id = Column(Integer, nullable=False)
    measurement_date = Column(String(30), nullable=False)
    measurement_datetime = Column(String(10))
    measurement_time = Column(String(10))
    measurement_type_concept_id = Column(Integer, nullable=False)
    operator_concept_id = Column(Integer)
    value_as_number = Column(Numeric)
    value_as_concept_id = Column(Integer)
    unit_concept_id = Column(Integer)
    range_low = Column(Numeric)
    range_high = Column(Numeric)
    provider_id = Column(Integer)
    visit_occurrence_id = Column(Integer)
    visit_detail_id = Column(Integer)
    measurement_source_value = Column(String(50))
    measurement_source_concept_id = Column(Integer, nullable=False)
    unit_source_value = Column(String(50))
    value_source_value = Column(String(50))


class Note(Base):
    __tablename__ = "note"

    # _id = Column(Integer, primary_key=True)
    note_id = Column(Integer, primary_key=True)
    person_id = Column(Integer, nullable=False)
    note_event_id = Column(Integer)
    note_event_field_concept_id = Column(Integer)
    note_date = Column(String(30), nullable=False)
    note_datetime = Column(String(10))
    note_type_concept_id = Column(Integer, nullable=False)
    note_class_concept_id = Column(Integer, nullable=False)
    note_title = Column(String(250))
    note_text = Column(Text, nullable=False)
    encoding_concept_id = Column(Integer, nullable=False)
    language_concept_id = Column(Integer, nullable=False)
    provider_id = Column(Integer)
    visit_occurrence_id = Column(Integer)
    visit_detail_id = Column(Integer)
    note_source_value = Column(String(50))


class NoteNLP(Base):
    __tablename__ = "note_nlp"

    note_nlp_id = Column(Integer, primary_key=True)
    note_id = Column(Integer, nullable=False)
    section_concept_id = Column(Integer)
    snippet = Column(String(250))
    offset = Column(String(50))
    lexical_variant = Column(String(250), nullable=False)
    note_nlp_concept_id = Column(Integer)
    note_nlp_source_concept_id = Column(Integer)
    nlp_system = Column(String(250))
    nlp_date = Column(String(30), nullable=False)
    nlp_datetime = Column(String(10))
    term_exists = Column(String(1))
    term_temporal = Column(String(50))
    term_modifiers = Column(String(2000))


class Observation(Base):
    __tablename__ = "observation"

    # _id = Column(Integer, primary_key=True)
    observation_id = Column(Integer, primary_key=True)
    person_id = Column(Integer, nullable=False)
    observation_concept_id = Column(Integer, nullable=False)
    observation_date = Column(String(30))
    observation_datetime = Column(String(10), nullable=False)
    observation_type_concept_id = Column(Integer, nullable=False)
    value_as_number = Column(Numeric)
    value_as_string = Column(String(60))
    value_as_concept_id = Column(Integer)
    qualifier_concept_id = Column(Integer)
    unit_concept_id = Column(Integer)
    provider_id = Column(Integer)
    visit_occurrence_id = Column(Integer)
    visit_detail_id = Column(Integer)
    observation_source_value = Column(String(50))
    observation_source_concept_id = Column(Integer, nullable=False)
    unit_source_value = Column(String(50))
    qualifier_source_value = Column(String(50))
    observation_event_id = Column(Integer)
    obs_event_field_concept_id = Column(Integer)
    value_as_datetime = Column(String(10))


class ObservationPeriod(Base):
    __tablename__ = "observation_period"

    # _id = Column(Integer, primary_key=True)
    observation_period_id = Column(Integer, primary_key=True)
    person_id = Column(Integer, nullable=False)
    observation_period_start_date = Column(String(30), nullable=False)
    observation_period_end_date = Column(String(30), nullable=False)
    period_type_concept_id = Column(Integer, nullable=False)


class PayerPlanPeriod(Base):
    __tablename__ = "payer_plan_period"

    # _id = Column(Integer, primary_key=True)
    payer_plan_period_id = Column(Integer, primary_key=True)
    person_id = Column(Integer, nullable=False)
    contract_person_id = Column(Integer)
    payer_plan_period_start_date = Column(String(30), nullable=False)
    payer_plan_period_end_date = Column(String(30), nullable=False)
    payer_concept_id = Column(Integer, nullable=False)
    payer_source_value = Column(String(50))
    payer_source_concept_id = Column(Integer, nullable=False)
    plan_concept_id = Column(Integer, nullable=False)
    plan_source_value = Column(String(50))
    plan_source_concept_id = Column(Integer, nullable=False)
    contract_concept_id = Column(Integer, nullable=False)
    contract_source_value = Column(String(50), nullable=False)
    contract_source_concept_id = Column(Integer, nullable=False)
    sponsor_concept_id = Column(Integer, nullable=False)
    sponsor_source_value = Column(String(50))
    sponsor_source_concept_id = Column(Integer)
    family_source_value = Column(String(50))
    stop_reason_concept_id = Column(Integer)
    stop_reason_source_value = Column(String(50))
    stop_reason_source_concept_id = Column(Integer)


class Person(Base):
    __tablename__ = "person"

    # _id = Column(Integer, primary_key=True)
    person_id = Column(Integer, primary_key=True)
    gender_concept_id = Column(Integer, nullable=False)
    year_of_birth = Column(Integer, nullable=False)
    month_of_birth = Column(Integer)
    day_of_birth = Column(Integer)
    # time_of_birth = Column(String(10))
    birth_datetime = Column(String(10))
    death_datetime = Column(String(10))
    race_concept_id = Column(Integer, nullable=False)
    ethnicity_concept_id = Column(Integer, nullable=False)
    location_id = Column(Integer)
    provider_id = Column(Integer)
    care_site_id = Column(Integer)
    person_source_value = Column(String(50))
    gender_source_value = Column(String(50))
    gender_source_concept_id = Column(Integer, nullable=False)
    race_source_value = Column(String(50))
    race_source_concept_id = Column(Integer, nullable=False)
    ethnicity_source_value = Column(String(50))
    ethnicity_source_concept_id = Column(Integer, nullable=False)


class ProcedureOccurrence(Base):
    __tablename__ = "procedure_occurrence"

    # _id = Column(Integer, primary_key=True)
    procedure_occurrence_id = Column(Integer, primary_key=True)
    person_id = Column(Integer, nullable=False)
    procedure_concept_id = Column(Integer, nullable=False)
    procedure_date = Column(String(30))
    procedure_datetime = Column(String(10), nullable=False)
    procedure_type_concept_id = Column(Integer, nullable=False)
    modifier_concept_id = Column(Integer)
    quantity = Column(Integer)
    provider_id = Column(Integer)
    visit_occurrence_id = Column(Integer)
    visit_detail_id = Column(Integer)
    procedure_source_value = Column(String(50))
    procedure_source_concept_id = Column(Integer, nullable=False)
    # qualifier_source_value = Column(String(50))
    modifier_source_value = Column(String(50))


class Provider(Base):
    __tablename__ = "provider"

    # _id = Column(Integer, primary_key=True)
    provider_id = Column(Integer, primary_key=True)
    provider_name = Column(String(255))
    npi = Column(String(20))
    dea = Column(String(20))
    specialty_concept_id = Column(Integer, nullable=False)
    care_site_id = Column(Integer)
    year_of_birth = Column(Integer)
    gender_concept_id = Column(Integer, nullable=False)
    provider_source_value = Column(String(50))
    specialty_source_value = Column(String(50))
    specialty_source_concept_id = Column(Integer, nullable=False)
    gender_source_value = Column(String(50))
    gender_source_concept_id = Column(Integer, nullable=False)


class Relationship(Base):
    __tablename__ = "relationship"

    # _id = Column(Integer, primary_key=True)
    relationship_id = Column(String(20), primary_key=True)
    relationship_name = Column(String(255), nullable=False)
    is_hierarchical = Column(String(1), nullable=False)
    defines_ancestry = Column(String(1), nullable=False)
    reverse_relationship_id = Column(String(20), nullable=False)
    relationship_concept_id = Column(Integer, nullable=False)


class SourceToConceptMap(Base):
    __tablename__ = "source_to_concept_map"

    _id = Column(Integer, primary_key=True)
    source_code = Column(String(50), nullable=False)
    source_concept_id = Column(Integer, nullable=False)
    source_vocabulary_id = Column(String(20), nullable=False)
    source_code_description = Column(String(255))
    target_concept_id = Column(Integer, nullable=False)
    target_vocabulary_id = Column(String(20), nullable=False)
    valid_start_date = Column(String(30), nullable=False)
    valid_end_date = Column(String(30), nullable=False)
    invalid_reason = Column(String(1))


class Speciman(Base):
    __tablename__ = "specimen"

    # _id = Column(Integer, primary_key=True)
    specimen_id = Column(Integer, primary_key=True)
    person_id = Column(Integer, nullable=False)
    specimen_concept_id = Column(Integer, nullable=False)
    specimen_type_concept_id = Column(Integer, nullable=False)
    specimen_date = Column(String(30), nullable=False)
    specimen_datetime = Column(String(10))
    quantity = Column(Numeric)
    unit_concept_id = Column(Integer)
    anatomic_site_concept_id = Column(Integer)
    disease_status_concept_id = Column(Integer)
    specimen_source_id = Column(String(50))
    specimen_source_value = Column(String(50))
    unit_source_value = Column(String(50))
    anatomic_site_source_value = Column(String(50))
    disease_status_source_value = Column(String(50))


class VisitDetail(Base):
    __tablename__ = "visit_detail"

    visit_detail_id = Column(Integer, primary_key=True)
    person_id = Column(Integer, nullable=False)
    visit_detail_concept_id = Column(Integer, nullable=False)
    visit_detail_start_date = Column(String(30), nullable=False)
    visit_detail_start_datetime = Column(String(10))
    visit_detail_end_date = Column(String(30), nullable=False)
    visit_detail_end_datetime = Column(String(10))
    visit_detail_type_concept_id = Column(Integer, nullable=False)
    provider_id = Column(Integer)
    care_site_id = Column(Integer)
    visit_detail_source_value = Column(String(50))
    visit_detail_source_concept_id = Column(Integer, nullable=False)
    admitted_from_concept_id = Column(String(50))
    admitted_from_source_value = Column(Integer, nullable=False)
    discharge_to_source_value = Column(String(50))
    discharge_to_concept_id = Column(Integer, nullable=False)
    preceding_visit_detail_id = Column(Integer)
    visit_detail_parent_id = Column(Integer)
    visit_occurrence_id = Column(Integer, nullable=False)


class VisitOccurrence(Base):
    __tablename__ = "visit_occurrence"

    # _id = Column(Integer, primary_key=True)
    visit_occurrence_id = Column(Integer, primary_key=True)
    person_id = Column(Integer, nullable=False)
    visit_concept_id = Column(Integer, nullable=False)
    visit_start_date = Column(String(30))
    visit_start_datetime = Column(String(10), nullable=False)
    visit_end_date = Column(String(30))
    visit_end_datetime = Column(String(10), nullable=False)
    visit_type_concept_id = Column(Integer, nullable=False)
    provider_id = Column(Integer)
    care_site_id = Column(Integer)
    visit_source_value = Column(String(50))
    visit_source_concept_id = Column(Integer, nullable=False)
    admitted_from_concept_id = Column(Integer, nullable=False)
    admitted_from_source_value = Column(String(50))
    discharge_to_concept_id = Column(Integer, nullable=False)
    discharge_to_source_value = Column(String(50))
    preceding_visit_occurrence_id = Column(Integer)


class Vocabulary(Base):
    __tablename__ = "vocabulary"

    # _id = Column(Integer, primary_key=True)
    vocabulary_id = Column(String(20), primary_key=True)
    vocabulary_name = Column(String(255), nullable=False)
    vocabulary_reference = Column(String(255), nullable=False)
    vocabulary_version = Column(String(255))
    vocabulary_concept_id = Column(Integer, nullable=False)
