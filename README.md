GraphQL Polars Dagster Example
==============================

This is an minimal example of how we could use [GraphQL](graphql.org)
to send data to a [Dagster](dagster.io) asset and then poll the run
via GraphQL as well.

A secondary goal is to make transformations on the dataset using a
streaming approach. So we would stream the CSV data from the frontend,
then stream it through Dagster using [Polars](pola.rs) or another
tool, and then persist it somewhere.
