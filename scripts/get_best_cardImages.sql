SELECT ImageUrl FROM cardImage
JOIN (
	SELECT CardId, MAX(Id) AS RevisionId
	FROM revision
	GROUP BY CardId
) as latestRevision ON latestRevision.RevisionId = cardImage.RevisionId
WHERE CardImageTypeId = 2