# Run performance tests based on environment
case "$ENV" in
    QA)
        pytest -v -n 2 -m "ats"
        ;;
    *)
        echo "Invalid marker"
        exit 1
        ;;
esac