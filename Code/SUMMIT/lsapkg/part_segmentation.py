#---------- PART SEGMENTATION MODULE ----------#
from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

# LIBRARIES NEEDED
import math 
import re
from nltk.tokenize import word_tokenize
from lsapkg import lsa_summarizer


class Part_Segmentation():

    def __call__(self, paragraphs):

        # SEGMENTATION
        title_headers = ['DECISION' , 'EN  BANC', 'RESOLUTION', 'D E C I S I O N' , 'E N  B A N C', 'R E S O L U T I O N']
        facts_headers = ['Facts', 'Antecedents', 'The Antecedents', 'The Factual Antecedents', 'Evidence for the Prosecution', 'Evidence for the defense', 'Ruling of the RTC', 'Ruling of the CA',
                        'The Charges', "The Defense's Version", "Defense's Version", "The Prosecution's Version", 'Proceedings Before the Court of Appeals', 'The Facts', 'Version of the Prosection',
                        'Version of the Defense', 'The Facts and the Case']
        issues_headers = ['The Issue', 'The Issues', 'The Issue Before the Court', 'The Issues Before the Court', 'Issue', 'Issues', 'The Present Petition', 'The Issue Presented', 'The Issues Presented']
        ruling_headers = ["Our Ruling", "The Ruling of the Court", "The Rulings of the Court", "The Ruling of this Court", "Proper Penalty", "The Court's Ruling"]


        facts_phrases = ['FACTS']
        issues_phrases = ['ISSUE', 'LONE ISSUE', 'WHETHER OR NOT', 'RAISE', 'RAISING', 'GUILT', 'CONVICT', 'ERR', 'COMMITTED ERROR', 'REASONABLE DOUBT']
        ruling_phrases = ['DECLARE', 'GRANT', 'DENIED', 'DISMISS', 'AFFIRM', 'GUILTY', 'NOT GUILTY', 'REVERSE', 'SETS ASIDE', 'SET ASIDE', 'ACQUITTED', 'ACQUITTAL', 'REINSTATED', 'MODIFICATION', 
                          'MODIFICATIONS', 'THE DECISION OF COURT', 'RULING', 'RULED', 'RENDERED', 'DECISION', 'DISPOSITIVE', 'MERIT', 'MERITORIOUS', 'SENTENCED', 'PENALTY', 
                          'EXEMPLARY DAMAGES', 'LIFE IMPRISONMENT', 'RECLUSION PERPETUA', 'GUILTY BEYOND REASONABLE DOUBT', 'REMANDED', 'ACCORDINGLY', 'RECALLED', 'DIRECTED', 'DISMISS']


        # VARIABLES
        facts_header = ""
        issues_header = ""
        ruling_header = ""

        title_sent = []
        noc_sent =[]
        facts_sent = []
        issues_sent = []
        ruling_sent = []

        issues_filtered = []
        ruling_filtered = []


         # IDENTIFICATION OF AVAILABLE HEADERS
        for headers in title_headers:
            for i, sentence in enumerate(paragraphs):
                if paragraphs[i].lower() == headers.lower():
                    title_header = paragraphs[i]

        for headers in facts_headers:
            for i, sentence in enumerate(paragraphs):
                if paragraphs[i].lower() == headers.lower():
                    facts_header = paragraphs[i]

        for headers in ruling_headers:
            for i, sentence in enumerate(paragraphs):
                if paragraphs[i].lower() == headers.lower():
                    ruling_header = paragraphs[i]

        for headers in issues_headers:
            for i, sentence in enumerate(paragraphs):
                if paragraphs[i].lower() == headers.lower():
                    issues_header = paragraphs[i]


        # TITLE SEGMENTATION
        for i, sentence in enumerate(paragraphs):
            if paragraphs[i] == title_header:
                break
            else:
                title_sent.append(paragraphs[i])

        # RULING SEGMENTATION
        if ruling_header:
            
            for sentence in paragraphs:
                if "concur." in sentence:
                    end_sent = sentence

            for headers in ruling_headers:
                for i, sentence in enumerate(paragraphs):
                    if paragraphs[i].lower() == headers.lower():
                        # while i < len(paragraphs) - 1:
                        while paragraphs[i] != end_sent:
                            ruling_sent.append(paragraphs[i])
                            i += 1

            for phrase in ruling_phrases:
                for sentence in ruling_sent:
                    if phrase in sentence:
                        if sentence not in ruling_filtered:
                            ruling_filtered.append(sentence)

            ruling_sent.extend(ruling_filtered)

        else:
            for phrase in ruling_phrases:
                for i, sentence in enumerate(paragraphs):
                    if phrase in sentence:
                        if sentence not in ruling_sent:
                            ruling_sent.append(sentence)
            
            ruling_header = ruling_sent[0]


        # ISSUES SEGMENTATION
        if issues_header:
            for headers in issues_headers:
                for i, sentence in enumerate(paragraphs):
                    if paragraphs[i].lower() == headers.lower():
                        while paragraphs[i] != ruling_header:
                            issues_sent.append(paragraphs[i])
                            i += 1
                        
            for phrase in issues_phrases:
                for sentence in issues_sent:
                    if phrase.lower() in sentence.lower():
                        if sentence not in issues_filtered:
                            issues_filtered.append(sentence)
        else:
            for phrase in issues_phrases:
                for i, sentence in enumerate(paragraphs):
                    if phrase in sentence:
                        if sentence not in issues_filtered:
                            issues_filtered.append(sentence)

            issues_header = issues_filtered [0]
                

        # FACTS SEGMENTATION
        if facts_header:
            for headers in facts_headers:
                for i, sentence in enumerate(paragraphs):
                    if paragraphs[i].lower() == headers.lower():
                        while paragraphs[i] != issues_header:
                            facts_sent.append(paragraphs[i])
                            i += 1
        else:
            for i, sentence in enumerate(paragraphs):
                if paragraphs[i] == issues_header:
                    break
                elif paragraphs[i] not in title_sent:
                    facts_sent.append(paragraphs[i])

        
        # NATURE OF CASE
        for i, sentence in enumerate(paragraphs):
             if paragraphs[i].lower() == title_header.lower():
                while paragraphs[i] != facts_header:
                    noc_sent.append(paragraphs[i])
                    i += 1

        
        # Sentence Count
        facts_count = math.floor(len(facts_sent) * 0.50)
        issues_count = len(issues_sent) if math.floor(len(issues_sent) * 0.05) == 0 else math.floor(len(issues_sent) * 0.05)
        ruling_count = math.floor(len(ruling_sent) * 0.45)

        # PRINTED EXTRACTED DATA
        print("\n\n----TITLE----\n\n")
        print(title_sent)

        print("\n\n----NATURE OF THE CASE----\n\n")
        print(noc_sent)

        print("\n\n----FACTS----\n\n")
        print(facts_sent)

        print("\n\n----ISSUES----\n\n")
        print(issues_sent)

        print("\n\n----RULING----\n\n")
        print(ruling_sent)

        print("\n\n----ISSUES FILTERED----\n\n")
        print(issues_filtered)

        print("\n\n----RULING FILTERED----\n\n")
        print(ruling_filtered)

        return title_sent, noc_sent, facts_sent, facts_count, issues_filtered, issues_count, ruling_sent, ruling_filtered, ruling_count


    # CLEANING OF SUMMARY
    def _cleaning_of_summary(self, title_sentences, noc_sentences, summary_facts, summary_issues, summary_ruling, ruling_fsentences):

        # TITLE 
        title = ""
        title_sentences = list(title_sentences)
        title_sent = []

        for sentence in title_sentences:
            if "G.R." in sentence:
                title_sent.append(sentence)
            if "VS." in sentence or "V." in sentence:
                title_sent.append(sentence)
        
        
        title = title_sent[0] + "\n" + title_sent[1]

        # NATURE OF CASE
        title_headers = ['DECISION' , 'EN  BANC', 'RESOLUTION', 'D E C I S I O N' , 'E N  B A N C', 'R E S O L U T I O N']
        noc = ""
        noc_sentences = list(noc_sentences)

        for sentence in noc_sentences:
            if ":" in sentence or sentence in title_headers:
                continue
            else:
                sentence = re.sub(r'\[[1234567890]*\]', "", sentence)
                noc += sentence

        # FACTS SUMMARY
        facts = ""
        summary_facts = list(dict.fromkeys(summary_facts))
        for sentences in summary_facts:
            sentences = re.sub(r'\[[1234567890]*\]', "", sentences)

            if len(word_tokenize(sentences)) > 4:
                facts += "• " + str(sentences) + "\n\n"
        
        # ISSUES SUMMARY
        issues = ""
        for sentences in summary_issues:
            sentences = re.sub(r'\[[1234567890]*\]', "", sentences)

            if len(word_tokenize(sentences)) > 4:
                issues += str(sentences) + "\n\n"

        # RULING SUMMARY
        ruling = ""

        # Filtered Sentences
        sentence_splitter = lsa_summarizer.LSA_Summarizer()._sentence_splitter
        ruling_fsentences = sentence_splitter(ruling_fsentences)

        
        summary_ruling = list(summary_ruling)
        summary_ruling.extend(ruling_fsentences)
        summary_ruling = list(dict.fromkeys(summary_ruling))
        for sentences in summary_ruling:
            sentences = re.sub(r'\[[1234567890]*\]', "", sentences)

            if len(word_tokenize(sentences)) > 4:
                ruling += str(sentences) + "\n\n"

        return title, noc, facts, issues, ruling    
        