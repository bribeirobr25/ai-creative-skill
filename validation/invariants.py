"""Small shared test oracles used by regression tests and isolated mutation probes."""
def publication_requires_authority(router):
    assert router.resolve('publique site').authority_gate is True

def paid_request_is_rejected(media, source):
    try:
        media.MediaRequest(source,128,96,allow_paid_submission=True).validate()
    except media.MediaError as exc:
        assert str(exc)=='PAID_SUBMISSION_BLOCKED'
    else:
        raise AssertionError('Paid request accepted by local-only helper')

def missing_fields_are_rejected(shape):
    assert shape.inspect('CONTENT_IDEA',{})['result']=='FAIL_STRUCTURAL'
