docker run --rm \
  --env PYTHON_POST_PROCESS_FILE='/usr/local/bin/black' \
  -v "${PWD}":/local openapitools/openapi-generator-cli generate \
   --git-repo-id checkedid-python-client \
   --git-user-id foarsitter \
  -i /local/openapi.json \
  -g python \
  -o /local \
  --additional-properties=packageName=checkedid \
  --additional-properties=packageVersion="${VERSION}"
